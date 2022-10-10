s1=input()
s1=s1.lower()
s2=input()
s2=s2.lower()
c=[]
r=0
for i in s1:
    if i not in s2:
        if i not in c:
            if i!=' ':
                c.append(i)
                r+=1
for i in s2:
    if i not in s1:
        if i not in c:
            if i!=' ':
                c.append(i)
                r+=1
print(r)