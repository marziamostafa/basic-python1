""" 
Write a Python code to remove characters from a string from 0 to n and return a new string.

For Example:
--> remove_chars("PYnative", 4) so output must be tive. Here, you need to remove the first four characters from a string.
--> remove_chars("PYnative", 2) so output must be native. Here, you need to remove the first two characters from a string.
 """

word='PYnative'
n=2
for i in range(n,len(word)):
    print(word[i],end='')