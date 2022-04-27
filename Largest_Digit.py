n=int(input())
large=0
while(n):
    d=n%10
    if(large<d):
        large=d
    n=n//10
print(large)