t=int(input())
for i in range(t):
    n=int(input())
    c=0
    a=list(map(int,input().split()))
    for i in a:
        if(i%2!=0):
            c+=1
    print(int(c/2))