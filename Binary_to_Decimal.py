t=int(input())
for i in range(t):
    s=0
    i=0
    s1=int(input())
    while(s1):
        d=s1%10
        s=s+d*pow(2,i)
        s1=s1//10
        i+=1
    print(s)