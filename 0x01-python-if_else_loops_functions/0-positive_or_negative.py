#!/usr/bin/python3
import random
number = random.randint(-100, 100)
print("The number:", number)
if number > 0:
    print("{}is positive".formart(number))
elif number == 0:
    print("{}is zero".format(number))
else:
    print("{}is negative".format())
