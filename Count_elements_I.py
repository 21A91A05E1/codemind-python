n,m=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
c=0
for i in l1:
    if i in l2:
        a.append(i)
    if(a.count(i)==1):
        c+=1
print(c)