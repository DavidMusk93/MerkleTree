import glob
import os

path = os.getcwd()

# get matched file path name one by one


def get_matched_file_path(path, file_type=''):
    f = glob.iglob(path + '/*' + file_type)
    for py in f:
        yield py


def clear_dir(path):
    files = get_matched_file_path(path)
    for file in files:
        os.remove(file)
        print("File '{}' is deleting...".format(file))

    print("The files in '{}' are removed.".format(path))


test_data_path = list(get_matched_file_path(path + '/data/', '.zip'))[0]
block_path = path + '/blocks/'


def get_metadata(path, file_type):
    # get file sizes and modification dates
    name_size_date = [(name, os.path.getsize(name), os.path.getatime(name))
                      for name in get_matched_file_path(path, file_type)]
    for name, size, mtime in name_size_date:
        print(name, size, mtime)


def get_file_list(path, category='all'):
    dic = {}
    # get all lists
    all_names = os.listdir(path)
    dic['all'] = all_names

    # get all regular files
    file_names = [name for name in os.listdir(path)
                  if os.path.isfile(os.path.join(path, name))]
    dic['file'] = file_names

    # get all dirs
    dir_names = [name for name in os.listdir(path)
                 if os.path.isdir(os.path.join(path, name))]
    dic['dir'] = dir_names

    return dic[category]

# padding block


def pad_block(block, block_size):
    while len(block) % block_size != 0:
        block += b'f' * (block_size - len(block))
    return block

# read a file block by block, default block size is 512K


def read_in_blocks(file_path, block_size=2 * 1024 * 1024):
    with open(file_path, 'rb') as f:
        # read entire file
        while True:
            block_data = f.read(block_size)
            if not block_data:
                break

            yield pad_block(block_data, block_size)

# make block name standard


def name_standardization(fixed_length, order):
    name = [str(order)]
    for _ in range(0, fixed_length - len(str(order))):
        name.insert(0, '0')

    return ''.join(name)

# saving blocks


import itertools


def save_blocks(blocks, target_path):
    # block name starts from 0
    i = 0
    fixed_length = 0

    # clone a generator object
    blocks1, blocks2 = itertools.tee(blocks)

    # get the length of blocks
    for _ in blocks1:
        fixed_length += 1

    fixed_length = len(str(fixed_length))
    # print(fixed_length)
    # print(blocks)
    # fix_length = len(str(len(blocks))) # generator has no len()
    for block in blocks2:
        # print(block)
        block_name = 'block' + name_standardization(fixed_length, i)
        block_path = target_path + block_name
        print('Write {}-th block...'.format(i))
        with open(block_path, 'wb') as f:
            f.write(block)
        i += 1

    print('All blocks were saved.')


# save_blocks(read_in_blocks(test_data_path), block_path)
