n=int(input())
for i in range(n-1,-1,-1):
    temp=i
    rev=0
    while(temp):
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    if(rev==i):
        bn=i
        a=n-bn
        break
for i in range(n+1,n+10000):
    temp=i
    rev=0
    while(temp):
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    if(rev==i):
        an=i
        b=an-n
        break
if(a==b):
    print(bn,an)
elif(a<b):
    print(bn)
else:
    print(an)