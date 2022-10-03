str=input()
s=str.split()
s1=[]
for i in s:
    s1.append(i[::-1])
print(*s1)