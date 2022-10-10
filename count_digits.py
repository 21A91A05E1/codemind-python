n=int(input())
a=list(map(int,input().split()))
for i in a:
    r=str(abs(i))
    print(len(r),end=' ')