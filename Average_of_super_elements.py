n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if(l.count(i)==i):
        if i not in a:
            a.append(i)
if(a==[]):
    print("-1")
else:
    avg=sum(a)/len(a)
    print("%.2f"%avg)