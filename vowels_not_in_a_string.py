s=input()
v='aeiou'
c=0
b=[]
for i in s:
    if i in v:
        b.append(i)
for i in v:
    if i not in b:
        print(i,end=' ')
        c+=1
if(c==0):
    print(0)