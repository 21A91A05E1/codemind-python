s=input().split()
b='aeiou'
e=[]
for i in s:
    c=0
    for j in i:
        if j in b:
            c+=1
    print(c,end=' ')