n=int(input())
rev=0
temp=n
while(n):
    d=n%10
    rev=rev*10+d
    n=n//10
if temp==rev:
    print('True')
else:
    print('False')