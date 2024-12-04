""" 
Write a Python program to print the first letter of your name using special character ‘*’.
Expected Output For M:

*     *
*     *
* * * *
*  *  *
*     *
*     *
*     *


 """

while i<7 :
  if i!=2 and i!=3:
   print('*     *')
  elif i==2:
    print('* * * *')
  else:
    print('*  *  *')
  i=i+1

    