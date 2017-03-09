import random
# this function is typically called by client who send a random integer
# which is from 0 to block counts to server


def generate_challenge(quantities):
    # avoid default random seed, update seed, it will generator same random number (for test)
    random.seed(b'davidmusk')  # seed based on byte data

    return random.randint(0, quantities)


if __name__ == '__main__':
    print(generate_challenge(82))
