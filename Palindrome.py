n=int(input())
rev=0
temp=n
while(temp):
    d=temp%10
    rev=rev*10+d
    temp=temp//10
if(rev==n):
    print("True")
else:
    print("False")
    