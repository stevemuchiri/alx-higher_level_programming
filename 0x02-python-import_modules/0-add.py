#!/usr/bin/python3
"""python import modules"""
a = 1
b = 2
add_0 = __import__("add_0")
print ("{} + {} = {}".format(a, b, add_0.add(a, b)))
