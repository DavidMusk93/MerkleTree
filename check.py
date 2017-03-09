# client receive response from server,
# then it check if native root value is equal to the
# calculated root value which is calculated by authentic path .
# by the way, client hold the root node and download the verified blcok form server.
import hash_function
import respond
import pickle
import challenge
import generate_blocks
import os


path = os.getcwd()
blocks_path = path + '/blocks/'

# get block quantities
block_quantities = len(generate_blocks.get_file_list(blocks_path))

# get challenge (actually, client owns challenge)
chal = challenge.generate_challenge(block_quantities)

# get verified block (like client download verified block from server)
verified_block = generate_blocks.get_file_list(blocks_path)[chal]

# get sha256 related to verified block
hash_value = hash_function.cal_file_sha256(blocks_path + verified_block)
# print(hash_value)

# get authentic path
authentic_path = respond.generate_respond(blocks_path, chal)

# load root note from native file
data_path = path + '/data/root_node'
with open(data_path, 'rb') as f:
    root = pickle.load(f)

# make sure left node value is beyond right node value
def right_order(hash ,node):
    order = [hash, node.get_value()]

    if node.get_id() % 2 == 0:
        order = list(reversed(order))

    return ''.join(order)

# the hash record the middle hash value
for node in authentic_path:
    hash_value = hash_function.cal_str_sha512(right_order(hash_value, node)) # left node value plus right node value

# check in if the data in server is integrity
if root.get_value() == hash_value:
    print('Server is good, the data is integrity.')
else:
    print('On, no... the data is not integrity!')

