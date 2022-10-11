s=input()
v='aeiou'
b=[]
c=0
for i in s:
    if i not in b:
        b.append(i)
for i in b:
    if i in v:
        c+=1
if(c==5):
    print('True')
else:
    print('False')
