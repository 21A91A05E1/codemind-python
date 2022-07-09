n=int(input())
a=list(map(int,input().split()))
k=int(input())
c=0
for i in range(len(a)):
    if(a[i]==k):
        print(i)
        c+=1
if(c==0):
    print("-1")