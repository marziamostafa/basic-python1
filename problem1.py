""" Suppose you have a floating number N.1 then,
Floor is the greatest integer less than or equal to N. And Ceil is the smallest
number greater than or equal to N.
Example: for 3.4 Floor is 3 and Ceil if 4.

Write a python program that takes a floating number from users using input() and
outputs both Floor and Ceil of that number. """

import math


number=float(input('Enter a floating number: '))
floor_number=int(number)
ceil_number=math.ceil(number)

print(floor_number)
print(ceil_number)