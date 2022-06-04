n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(len(a)):
    dc=0
    while(a[i]):
        d=a[i]%10
        a[i]=a[i]//10
        dc+=1
    if(dc%2==0):
        c+=1
print(c)