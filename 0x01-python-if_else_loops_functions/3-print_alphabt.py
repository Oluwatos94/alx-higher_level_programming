#!/usr/bin/python3
for char in range(26):
    if char != 4 and char != 16:
        print(f"{:s}".format(chr(char + ord("a"))), end="")
