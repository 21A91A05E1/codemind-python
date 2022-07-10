n=int(input())
m=int(input())
for i in range(n,m+1):
    temp=i
    c=0
    sc=0
    while(temp):
        d=temp%10
        temp=temp//10
        c+=1
        if(d==0):
            break
        if(i%d==0):
            sc+=1
    if(sc==c):
        print(i,end=' ')