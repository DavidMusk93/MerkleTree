import merkle_tree
import generate_tags
import os

# test vriables
path = os.getcwd()
blocks_path = path + '/blocks/'


def generate_merkle_tree(path):
    # get leafs hash tags
    tags_dict = generate_tags.generate_blcok_tags(path)
    tags = list(tags_dict.values())
    # print(tags)

    tree = merkle_tree.generate_tree(tags)

    return tree


if __name__ == '__main__':
    tree = generate_merkle_tree(blocks_path)

    import pickle

    # save root node by serializing node object
    with open('data/root_node', 'wb') as f:
        pickle.dump(tree['root'], f)
