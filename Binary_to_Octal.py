t=int(input())
for i in range(t):
    n=int(input())
    i=0
    dec=0
    while(n):
        d=n%10
        dec=dec+d*pow(2,i)
        n=n//10
        i+=1
    print(oct(dec)[2::])