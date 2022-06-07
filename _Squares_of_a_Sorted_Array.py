n=int(input())
a=list(map(int,input().split()))
c=list()
for i in a:
    i=i**2
    c.append(i)
print(*sorted(c))