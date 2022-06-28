n=int(input())
a=list(map(int,input().split()))
c=0
res=set(a)
for i in res:
    if(i%2==0):
        c+=1
print(c)