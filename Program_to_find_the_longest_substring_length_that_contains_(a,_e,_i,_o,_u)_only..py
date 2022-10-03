str=input()
c=0
max=0
v='aeiouAEIOU'
for i in range(len(str)):
    c=0
    for j in range(i,len(str)):
        if str[j] in v:
            c+=1
            if(max<c):
                max=c
        else:
            break
print(max)