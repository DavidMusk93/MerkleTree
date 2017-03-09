import hashlib

# read stuff in 64Kb
BUF_SIZE = 2 ** 16


# caculate sha256 for a file
def cal_file_sha256(file):
    sha256 = hashlib.sha3_256()

    with open(file, 'rb') as f:
        while True:
            # use buffers to not use tons of memory
            data = f.read(BUF_SIZE)
            if not data:
                break

            sha256.update(data)

        return sha256.hexdigest()


def cal_str_sha512(str_proto):
    sha512 = hashlib.sha3_512()

    bytes_form = str.encode(str_proto)
    sha512.update(bytes_form)

    return sha512.hexdigest()


if __name__ == '__main__':
    print(cal_str_sha512('smq'))