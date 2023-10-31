#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = 'Last digit of'
str1 = 'is'
x = number % 10
if x > 5:
    print(str, number, str1, x, "and is greater than 5")
if x == 0:
    print(str, number, str1, x, "and is 0")
if x < 6 and x != 0:
    print(str, number, str1, x, "and is less than 6 and not 0")
