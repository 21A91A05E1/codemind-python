n=int(input())
i=0
dec=0
while(n):
    d=n%10
    dec=dec+d*pow(8,i)
    i+=1
    n=int(n/10)
print(bin(dec)[2:])
    