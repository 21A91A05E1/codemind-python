n=int(input())
for i in range(0,n):
    for j in range(n-1,1,-1):
        c=0
        for k in range(1,j+1):
            if j%k==0:
                c+=1
        if(c==2):
            cp=j
            a=n-cp
            break
    for j in range(n,n+50):
        c=0
        for k in range(1,j+1):
            if j%k==0:
                c+=1
        if(c==2):
            cp1=j
            b=cp1-n
            break
if(a<b):
    print(a)
else:
    print(b)