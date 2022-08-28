a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
a=[]
for i in l1:
    if i in l2:
        a.append(i)
    if(a.count(i)==1):
        print(i,end=' ')