def prime(n):
    for i in range(2,int((n**0.5)+1)):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
b=int(input())
r=a+b
for j in range(1,10):
    r1=r+j
    if(prime(r1)):
        print(j)
        break