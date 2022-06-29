#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstDigit = abs(number) % 10


def lastnum(num):
    if num < 0:
        num = -num
    if (num > 5):
        return "and is greater than 5"
    elif (num != 0 & num < 6):
        return "and is less than 6 and not 0"
    elif (num == 0):
        return "and is 0"


print("Last digit of {:d} is {:d} {}".format(number, lstDigit, lastnum(lstDigit)))
