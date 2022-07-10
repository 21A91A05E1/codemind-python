n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(len(a)):
    temp=a[i]
    while(temp):
        d=temp%10
        sum=sum+d
        temp=temp//10
print(sum)