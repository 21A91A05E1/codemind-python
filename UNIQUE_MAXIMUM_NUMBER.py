n=int(input())
c=0
c1=0
max=0
a=list(map(int,input().split()))
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(a[i]==a[j] and i!=j):
            c+=1
    if(c==0):
        if(a[i]>max):
            max=a[i]
            c1+=1
if(c1>0):
    print(max)
else:
    print('-1')
    