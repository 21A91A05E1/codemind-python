import math
n=int(input())
sum=0
a=list(map(int,input().split()))
for i in a:
    s=int(math.sqrt(i))
    if(i==s*s):
        sum=sum+i
print(sum)
    