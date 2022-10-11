n=int(input())
a=list(map(int,input().split()))
j=0
s=0
for i in range(len(a)-1,-1,-1):
    s=s+a[i]*pow(2,j)
    j+=1
print(s)