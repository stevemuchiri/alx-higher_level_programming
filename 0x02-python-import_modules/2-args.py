#!/usr/bin/python3
if __name__ == "__main__":
    """ numbe r  of  arguments"""
    import sys

    num_args = len(sys.argv) - 1
    if num_args == 0:
        print("0 argument.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(num_args))

    for i in range(num_args):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
