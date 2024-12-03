""" Write a function that takes 3 integer inputs from user and
outputs absolute values of these integers without using any
library functions.

Sample Input:                             Sample output:
-100                                        100
234                                         234
-350                                        350 

"""

# num1=int(input('Enter integer number1'))
# num2=int(input('Enter integer number1'))
# num3=int(input('Enter integer number1'))

num=1
while num<=3:
    number=int(input('Enter a integer number: '))
    if number<0:
        print(-number)
    else:
        print(number)