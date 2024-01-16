#!/usr/bin/python3

def print_last_digit(number):
    """
    Prints the last digit of a number and returns its value.

    Parameters:
    - number: an integer

    Returns:
    - The value of the last digit
    """
    last_digit = abs(number) % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
