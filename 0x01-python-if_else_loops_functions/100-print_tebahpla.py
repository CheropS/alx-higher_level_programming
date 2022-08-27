#!/usr/bin/python3

j = 0
for c in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(c - 1)), end="")
    j = 32 if j == 0 else 0
