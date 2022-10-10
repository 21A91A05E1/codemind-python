t=int(input())
a=list(map(int,input().split()))
n=int(input())
b=list(map(int,input().split()))
r=[]
for i in range(t):
    r.insert(b[i],a[i])
for i in range(t):
    print(r[i],end=' ')