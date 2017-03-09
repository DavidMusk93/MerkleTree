import generate_blocks
import hash_function
from collections import OrderedDict

# test path
root_path = generate_blocks.path
blocks_path = root_path + '/blocks/'


def generate_blcok_tags(path):
    # the form of block tags is a ordered dictionary
    block_tags = OrderedDict()

    # get blocks list
    blocks_list = generate_blocks.get_file_list(path, 'file')
    # print(blocks_list)
    for block_name in blocks_list:
        blocks_path = path + block_name
        block_tag = hash_function.cal_file_sha256(blocks_path)
        block_tags[block_name] = block_tag

    return block_tags


if __name__ == '__main__':
    print(generate_blcok_tags(blocks_path))
