#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    num_args = len(argv) -1

    if num_args == 0:
        print("0 argument.")
    elif num_args == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(num_args))

    for i in range(1, num_args + 1):
        print("{}: {}".format(i, argv[i]))

