n=int(input())
fact=0
for i in range(1,n+1):
    if(n%i==0):
        fact+=1
if(fact==2):
    print('prime')
else:
    print('not a prime')