t=int(input())
c=0
for i in range(t):
    m=int(input())
    a=list(map(int,input().split()))
    for j in range(1,m+1):
        if(a.count(j)==0):
            print(j)