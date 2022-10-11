s=input()
v='aeiouAEIOU'
c=0
b=[]
for i in s:
    if i not in b:
        b.append(i)
for i in b:
    if i in v:
        print(i,end=' ')
        c+=1
if(c==0):
    print('-1')