#!/usr/bin/python3

"""prints the alphabet in lower case, not followed by a new line,\
        except q and e"""

for letter in range(97, 123):
    if chr(letter) != 'q' and chr(letter) != 'e':
        print("{}".format(chr(letter)), end="")
