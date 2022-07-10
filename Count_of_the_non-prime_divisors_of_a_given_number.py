n=int(input())
c1=1
for i in range(1,n+1):
    c=0
    if(n%i==0):
        for j in range(2,n):
            if(i%j==0):
                c+=1
    if(c>1):
        c1+=1
print(c1)