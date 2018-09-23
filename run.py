# -*-coding:utf-8-*-
# !/usr/bin/python3
"""
Read data from unix format file

Sept 23, 2018
@author: shoujiangma@163.com
"""
import sys

import huffman_tree as huffman_tree

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Too few parameters. Usage example: ./run.py file_name")
        exit(0)

    INPUT_FILE = sys.argv[1]
    ENCODE_FILE = INPUT_FILE + ".enc"
    DECODE_FILE = INPUT_FILE + ".dec"

    # compress org file by huffman coding
    huffman_tree.compress(INPUT_FILE, ENCODE_FILE)
    print("compress done.\n")

    # TODO: encrypt compressed file

    # TODO: decrypt bin file

    # decompress file
    huffman_tree.decompress(ENCODE_FILE, DECODE_FILE)
    print("decompress done.\n")
