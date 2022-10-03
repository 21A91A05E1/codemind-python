def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
res=a+b
for j in range(1,10):
    res1=res+j
    if(prime(res1)):
        print(j)
        break
        