str=input().split()
a=[]
for i in range(len(str)):
    if((i)%2==0):
        a.append(str[i][::-1])
    else:
        a.append(str[i])
print(*a)