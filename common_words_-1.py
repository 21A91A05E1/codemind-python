s1=input()
s1=s1.lower()
a=s1.split()
s2=input()
s2=s2.lower()
b=s2.split()
c=0
for i in a:
    if i in b:
        c+=1
print(c)