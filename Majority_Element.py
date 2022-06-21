n=int(input())
a=list(map(int,input().split()))
max=0
for i in range(len(a)):
    c=0
    for j in range(len(a)):
        if(a[i]==a[j] and i!=j):
            c+=1
    if(c>max):
        max=c
        maxelement=a[i]
print(maxelement)