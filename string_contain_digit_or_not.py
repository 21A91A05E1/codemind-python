str=input()
c=0
for i in str:
    if i in '0123456789':
        c+=1
if(c>0):
    print("Contains %d digit"%c)
else:
    print("Doesn't contain digit")