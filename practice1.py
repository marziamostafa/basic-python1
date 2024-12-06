""" 
Clean the data and get a String output 'a e i o u'
 """
data="aNtEriOur\n\t>>"
lower_data=data.lower()
print(lower_data)

for c in lower_data:
    if (c=='a') or (c=='e') or (c=='i') or (c=='o') or (c=='u'):
        print(c, end=' ')
