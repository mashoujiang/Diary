# -*-coding:utf-8-*-
# !/usr/bin/python3
"""
Read data from unix format file

Sept 23, 2018
@author: shoujiangma@163.com
"""
import sys
from binascii import b2a_hex

from Cryptodome import Random
from Cryptodome.Cipher import AES

import huffman_tree as huffman_tree


def encrypt(in_file, out_file, key):
    with open(in_file, 'rb') as inputf, open(out_file, 'wb') as outputf:
        data = inputf.read()
        iv = Random.new().read(AES.block_size)

        mycipher = AES.new(key, AES.MODE_CFB, iv)
        ciphertext = iv + mycipher.encrypt(data)

        print("key:", key)
        print("iv:", b2a_hex(ciphertext)[:16])
        # print("encrypt data:", b2a_hex(ciphertext)[16:])

        outputf.write(ciphertext)


def decrypt(in_file, out_file, key):
    with open(in_file, 'rb') as inputf, open(out_file, 'wb') as outputf:
        ciphertext = inputf.read()
        mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
        decrypttext = mydecrypt.decrypt(ciphertext[16:])

        print("key:", key)
        print("iv:", ciphertext[:16])
        # print("decrypt data:", decrypttext)
        outputf.write(decrypttext)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Too few parameters. Usage example: ./run.py file_name KEY")
        exit(0)

    INPUT_FILE = sys.argv[1]
    ENCODE_FILE = INPUT_FILE + ".encode"
    DECODE_FILE = INPUT_FILE + ".decode"
    ENCRYPT_FILE = INPUT_FILE + ".encrypt"
    DECRYPT_FILE = INPUT_FILE + ".decrypt"
    KEY = sys.argv[2].encode()

    # compress org file by huffman coding
    huffman_tree.compress(INPUT_FILE, ENCODE_FILE)
    print("compress done.\n")

    # TODO: encrypt compressed file
    encrypt(ENCODE_FILE, ENCRYPT_FILE, KEY)

    # TODO: decrypt bin file
    decrypt(ENCRYPT_FILE, DECRYPT_FILE, KEY)

    # decompress file
    huffman_tree.decompress(DECRYPT_FILE, DECODE_FILE)
    print("decompress done.\n")
