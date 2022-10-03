s=input()
b=s.lower()
ind=0
c1=0
for i in range(len(b)):
    c=0
    for j in range(len(b)):
        if(i!=j and b[i]==b[j]):
            c+=1
    if(c==0):
        ind=i
        c1+=1
        break
if(c1==0):
    print("-1")
else:
    print(ind)