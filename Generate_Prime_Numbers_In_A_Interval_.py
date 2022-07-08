a=int(input())
b=int(input())
fact=0
for i in range(a,b+1):
    fact=0
    for j in range(1,i+1):
        if(i%j==0):
            fact+=1
    if(fact==2):
        print(i)