import hash_function


# node class represents the merkle tree node
class Node:
    def __init__(
            self,
            node_id,
            value,
            parent_node=None,
            left_node=None,
            right_node=None):
        self._node_id = node_id
        self._value = value
        self.parent_node = parent_node
        self.left_node = left_node
        self.right_node = right_node

    def get_id(self):
        return self._node_id

    def get_value(self):
        return self._value

    def get_parent_node(self):
        return self.parent_node

    def get_sibling(self):
        return self.parent_node.left_node if self.parent_node.left_node.get_id(
        ) != self._node_id else self.parent_node.right_node

    def set_parent(self, node):
        self.parent_node = node


test = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

import math


# generate merkle tree depth through block quantities
def generate_depth(block_quantities):
    length = len(block_quantities)
    len_log = math.log2(length)
    depth = int(len_log)
    return depth + 1 if depth < len_log else depth


# generate constant difference between parent id and left child id which
# divides 2
# def generate_diff(block_quantities):
#    depth = generate_depth(block_quantities)
#    return pow(2, depth)

# use test will lead to id sequence error
# diff = generate_diff(test)


# generate leaf nodes
def generate_leafs(hash_value_list, depth):
    leafs = []
    i = 0  # id growth from 0

    # solid value
    for hash_value in hash_value_list:
        node = Node(i, hash_value)
        leafs.append(node)
        i += 1

    # blank value
    for padding_id in range(len(hash_value_list), 2 ** depth):
        node = Node(padding_id, 'f' * 64)
        leafs.append(node)

    return leafs


# merkle_tree['leafs'] = generate_leafs(test, generate_depth(test))

# generate parent value based on children values
# to be simplified, just add two values
# def hash_function(v1, v2):
#     return v1 + v2


# two children node generate parent node
def generate_parent(left_node, right_node, depth):
    parent_id = left_node.get_id() // 2 + 2 ** depth
    parent_value = hash_function.cal_str_sha512(
        left_node.get_value() +
        right_node.get_value())  # the order of siblings would influence the check-in step
    parent_node = Node(parent_id, parent_value, None, left_node, right_node)

    # find father for children
    # one question: can this way change the children's value
    left_node.set_parent(parent_node)
    right_node.set_parent(parent_node)

    return parent_node


# generate middle nodes, related to its bottom level nodes
def generate_upper_level(bottom_nodes, depth):
    # get the nodes quantities
    length = len(bottom_nodes) // 2

    nodes = []

    for i in range(0, length):
        node = generate_parent(
            bottom_nodes[i * 2], bottom_nodes[i * 2 + 1], depth)
        nodes.append(node)

    return nodes


from collections import OrderedDict


# make sure the middle levels are ordered

# get the last value for ordered dictionary


def get_last_value(d):
    return next(reversed(d.items()))[1]


# generate merkle tree
def generate_tree(test):
    depth = generate_depth(test)
    merkle_tree = {'leafs': [], 'mids': OrderedDict(), 'root': None}

    # generate leaf nodes
    merkle_tree['leafs'] = generate_leafs(test, depth)
    # bottom nodes
    bottom_nodes = merkle_tree['leafs']
    # generate all middle node
    for i in range(0, depth - 1):
        level_name = 'level' + str(i + 1)
        level_nodes = generate_upper_level(bottom_nodes, depth)
        merkle_tree['mids'][level_name] = level_nodes

        # update bottom nodes for each iteration
        bottom_nodes = get_last_value(merkle_tree['mids'])

    # generate root node
    merkle_tree['root'] = generate_upper_level(bottom_nodes, depth)[0]

    return merkle_tree


if __name__ == '__main__':
    merkle_tree = generate_tree(test)
    print(merkle_tree)
