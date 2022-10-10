t=int(input())
a=list(map(int,input().split()))
for i in range(0,t-1,2):
    for j in range(a[i]):
        print(a[i+1],end=' ')