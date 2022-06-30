str=input()
c=0
for i in str:
    if str.count(i)>1:
        c+=1
if(c==0):
    print('True')
else:
    print('False')