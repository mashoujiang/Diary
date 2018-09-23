# -*-coding:utf-8-*-
# !/usr/bin/python3
"""
Read data from unix format file

Sept 23, 2018
@author: shoujiangma@163.com
"""
import sys

from Cryptodome.Cipher import AES

import huffman_tree as huffman_tree


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
        print("Too few parameters. Usage example: ./run_decode_decrypt.py file_name KEY")
        exit(0)

    ENCRYPT_FILE = sys.argv[1]
    DECRYPT_FILE = ENCRYPT_FILE[:-8] + ".decrypt"
    DECODE_FILE = ENCRYPT_FILE[:-8] + ".decode"
    KEY = sys.argv[2].encode()

    # decrypt bin file
    decrypt(ENCRYPT_FILE, DECRYPT_FILE, KEY)

    # decompress file
    huffman_tree.decompress(DECRYPT_FILE, DECODE_FILE)
    print("decompress done.\n")
