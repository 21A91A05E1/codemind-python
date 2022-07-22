a=list(map(int,input().split()))
max=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        p=(a[i]-1)*(a[j]-1)
        if(p>max):
            max=p
print(max)