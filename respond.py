# after receiving a challenge, the server invokes this
# function to generate a respond to client
import generate_tree
import challenge
import generate_blocks
import os


path = os.getcwd()
blocks_path = path + '/blocks/'
# get block quantities
block_quantities = len(generate_blocks.get_file_list(blocks_path))

# get challenge (to simulate the progress, the server generator challenge)
chal = challenge.generate_challenge(block_quantities)


def generate_respond(path, chal=chal):
    # generate merkle tree
    tree = generate_tree.generate_merkle_tree(path)

    # get the depth of merkle tree
    depth = len(tree['mids']) + 1

    verified_block = tree['leafs'][chal]

    # generate respond
    for _ in range(0, depth):
        yield verified_block.get_sibling()
        # go to next level
        verified_block = verified_block.get_parent_node()


if __name__ == '__main__':

    respond = generate_respond(blocks_path)
    for node in respond:
        print(node.get_id())
        print(node.get_value())
