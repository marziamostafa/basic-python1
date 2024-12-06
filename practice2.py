""" 
Encrypt the following code so that no one can get your energy
 """

data="firebaby"
shift=4

for c in data:
    encrypted=(ord(c)+shift-97)%26+97
    output=chr(encrypted)
    print(output,end=' ')