n=int(input())
m=int(input())
c=0
for i in range(n,m):
    temp=i
    rev=0
    while(temp):
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    if(i==rev):
        print(i,end=' ')