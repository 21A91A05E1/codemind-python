n=int(input())
a=list(map(int,input().split()))
c=0
maxi=0
for i in a:
    r=str(i)
    if(len(r)>maxi):
        maxi=len(r)
for i in a:
    if len(str(i))==maxi:
        c+=1
print(c)
