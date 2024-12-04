""" 
Write a Python code to accept a string from the user and display characters present at an even index number.

For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

 """

string=input('Enter a word: ')
i=1
for i in range(len(string)):
   
    if i%2==0:
        print(string[i],end=' ')
    else:
        continue