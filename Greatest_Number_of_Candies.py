n=int(input())
a=list(map(int,input().split()))
m=int(input())
for i in range(n):
    if((a[i]+m)>=max(a)):
        print('True',end=' ')
    else:
        print('False',end=' ')