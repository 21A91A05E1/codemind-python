a,b=map(int,input().split())
n=list(map(int,input().split()))
sum=0
c=0
for i in range(0,a):
    for j in range(i,a):
        sum=sum+n[j]
        if(sum==b):
            c+=1
        if(sum>b):
            break
    sum=0
print(c)
    