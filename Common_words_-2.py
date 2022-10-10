s1=input()
s1=s1.lower()
a=s1.split()
s2=input()
s2=s2.lower()
b=s2.split()
c=[]
d=[]
r=0
for i in a:
    if a.count(i)==1:
        c.append(i)
for i in b:
    if b.count(i)==1:
        d.append(i)
for i in c:
    if i in d:
        r+=1
print(r)