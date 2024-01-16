#!/usr/bin/python3
def pow(a, b):
    """
    Computes a to the power of b and returns the value.

    Parameters:
    - a: a base number (float or integer)
    - b: an exponent (integer)

    Returns:
    - The value of a ^ b
    """
    result = 1
    for _ in range(abs(b)):
        result *= a

    return 1 / result if b < 0 else result
