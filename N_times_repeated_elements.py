n=int(input())
a=list(map(int,input().split()))
k=int(input())
b=[]
for i in a:
    if(a.count(i)==k):
        b.append(i)
    if(b.count(i)==1):
        print(i,end=' ')
if(b==[]):
    print("-1")