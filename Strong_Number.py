n=int(input())
fact=1
sum=0
temp=n
while(n):
    d=n%10
    for i in range(1,d+1):
        fact=fact*i
    sum=sum+fact
    fact=1
    n=n//10
n=temp
if(sum==n):
    print('The number %d is a strong number'%n)
else:
    print('The number %d is not a strong number'%n)
    
    