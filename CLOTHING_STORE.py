n=int(input())
sum=0
a=list(map(int,input().split()))
for i in range(len(a)):
    c=0
    for j in range(i+1,len(a)):
        if(a[i]==a[j]):
            c+=1
    sum=sum+c%2
print(sum)