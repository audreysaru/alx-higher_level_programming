#!/usr/bin/python3
def uppercase(input_str):
    for char in input_str:
        if 97 <= ord(char) <= 122:
            print(chr(ord(char) - 32), end='')
        else:
            print(char, end='')
    print()
