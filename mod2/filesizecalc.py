#!/usr/bin/env python3

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = filesize//4096
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % 4096
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return 4096*(full_blocks+1)
    return full_blocks * 4096


number = calculate_storage(int(input("Enter a number: ")))

print(number)
