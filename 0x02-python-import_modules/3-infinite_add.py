#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv[1:]

    if not args:
        print("0")
    else:
        result = sum(map(int, args))
        print(result)
