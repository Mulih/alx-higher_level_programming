#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = 'last digit of'
str1 = 'is'
if number <= 5:
    print(str, number, str1, 'and is greater than 5')
elif number >= 6 and number != 0:
    print(str, number, 'is', number, str1, 'and is less than 6 and not 0')
else:
    print(str, number, str1, 'is zero')
