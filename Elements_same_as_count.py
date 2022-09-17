n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if(l.count(i)==i):
        a.append(i)
    if(a.count(i)==1):
        b.append(i)
if(a==[]):
    print("-1")
else:
    print(*b,end=' ')