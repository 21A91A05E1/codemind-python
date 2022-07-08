n=int(input())
for i in range(n):
    t=int(input())
    temp=t
    rev=0
    while(temp):
        d=temp%10
        rev=rev*10+d
        temp=temp//10
    if(t==rev):
        print('True')
    else:
        print('False')