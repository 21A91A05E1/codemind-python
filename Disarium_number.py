import math
n=int(input())
sum=0
dc=0
temp=n
while(temp):
    temp=temp//10
    dc+=1
temp=n
while(temp):
    d=temp%10
    sum=sum+pow(d,dc)
    temp=temp//10
    dc-=1
if(sum==n):
    print('True')
else:
    print('False')
    