str=input()
s1=input()
c=0
for i in (str):
    if i in 'aeiouAEIOU':
        if s1 in i:
            c+=1
if(c!=0):
    print('True')
    print(str.index(s1))
else:
    print('False')