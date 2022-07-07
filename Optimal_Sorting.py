n=int(input())
c=0
for i in range(n):
    m=int(input())
    a=list(map(int,input().split()))
    for j in range(1,m):
        if(a[j-1]>a[j]):
            c+=1
    if(c==0):
        print(c)
    else:
        ma=max(a)
        mi=min(a)
        print(ma-mi)