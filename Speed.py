t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    c=1
    for i in range(n-1):
        if(a[i+1]<a[i]):
            c+=1
    print(c)