n=int(input())
sum=0
while(n//10!=0):
    sum=0
    while(n):
        d=n%10
        sum=sum+d
        n=n//10
    n=sum
print(sum)