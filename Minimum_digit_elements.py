n=int(input())
a=list(map(int,input().split()))
c=0
mini=100
for i in a:
    r=str(i)
    if(len(r)<mini):
        mini=len(r)
for i in a:
    if len(str(i))==mini:
        c+=1
print(c)