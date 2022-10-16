s=input().split()
b='aeiou'
e=[]
c1=0
for i in s:
    c=0
    for j in i:
        if j in b:
            c+=1
    e.append(c)
for i in e:
    if i==max(e):
        c1+=1
print(c1)