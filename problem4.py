""" 
Write a Python program to check if user entered number is ZERO, POSITIVE or
NEGATIVE until user does not want to quit.
User will type ‘Quit’ to close the program.

Sample:
> Enter input: 2
> 2 is positive
> -3
> -3 is negative
> “Quit”
> (stop the program)
 """


number=True

while number:
    num=input('Enter a number: ')
    print(type(num))
   
    if num=='quit':
      number=False
    elif num.isidentifier():
      print('to stop type quit')
      continue
    elif float(num).is_integer():
     number=True
     n=float(num)
     print('yes')
    
    else:
      print('to stop type quit')
      
      

    if number:
      if n>0:
       print('Positive number')
      elif n<0:
       print('Negative number')
      else:
       print('Zero')
    else:
      print('stopped')
      break
     


  
    
