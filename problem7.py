""" 
Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

Given 1:                                       Given 2:
number1 = 20                                   number1 = 40
number2 = 30                                   number2 = 30


Expected Output:                               Expected Output:
The result is 600                              The result is 70
 """

number1=20
number2=30
product=number1*number2
sum=number1+number2

if product<=1000:
    print('Product is: ',product)
else:
    print('Sum is: ',sum)