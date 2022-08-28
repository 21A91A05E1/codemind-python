n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for i in l:
    if(l.count(i)==i):
        a.append(i)
    if(a.count(i)==1):
        b.append(i)
if(b==[]):
    print("-1")
else:
    avg=sum(b)/len(b)
    print("%.2f"%avg)