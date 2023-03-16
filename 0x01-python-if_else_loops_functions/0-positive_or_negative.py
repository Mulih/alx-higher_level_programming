#!/usr/bin/python3
import random
number = random.randint(-10, 10)

for number in range(-10, 10):
	if number % 2 < 0:
		print(number, 'is negative')
		continue
		if number % 2 == 0:
			print(number, 'is zero')
			break		
		else:
			print(number, 'is positive')
