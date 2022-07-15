x=int(input())
c=0
b=[]
for i in range(x):
    z=int(input())
    b.append(z)
y=int(input())
for j in b:
    if j<=y:
        c+=1
    else:
        c+=2
print(c)