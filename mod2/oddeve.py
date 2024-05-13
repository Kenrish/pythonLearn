#!/usr/bin/env python3

def is_even(number):
    if number % 2 == 0:
        return True
    return False


check = is_even(int(input("Enter the number to verify: ")))

print(check)
