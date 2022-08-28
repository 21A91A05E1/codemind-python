n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
c=0
for i in l1:
    if i not in l2:
        a.append(i)
    if(a.count(i)==1):
        c+=1
for j in l2:
    if j not in l1:
        a.append(j)
    if(a.count(j)==1):
        c+=1
print(c)