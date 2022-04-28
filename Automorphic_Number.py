n=int(input())
count=1
sq=n*n
temp=n
while(n!=0):
    count=count*10
    n=n//10
if(sq%count==temp):
    print('Automorphic Number');
else:
    print('Not an Automorphic Number');