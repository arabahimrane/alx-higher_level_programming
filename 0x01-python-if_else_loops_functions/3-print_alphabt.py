#!/usr/bin/python3
for c in range(97, 123):
    if (c != ord('q') and c != ord('e')):
        print("{:s}".format(chr(c)), end='')
