n=int(input())
a=list(map(int,input().split()))
c=0
res=0
for i in range(len(a)):
    if(a[i]==1):
        c+=1
    else:
        res=max(res,c)
        c=0
if(c>res):
    print(c)
else:
    print(res)