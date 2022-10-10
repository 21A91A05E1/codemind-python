n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(sorted(a))):
    if(a[i]==k):
        print(i,end=' ')
        c=1
        break
for i in range(n-1,-1,-1):
    if(a[i]==k):
        print(i,end=' ')
        c=1
        break
if(c==0):
    print('-1 -1')