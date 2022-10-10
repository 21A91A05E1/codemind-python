t=int(input())
a=list(map(int,input().split()))
r=0
for i in range(0,t):
    for j in range(i,t):
        if(r<a[j]-a[i]):
            r=a[j]-a[i]
print(r)