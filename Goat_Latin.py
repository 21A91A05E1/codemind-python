s=input().split()
v='aeiou'
b=[]
c=1
for i in s:
    if i[0] in v:
        res=i+'ma'+'a'*c
    else:
        res=i[1::]+i[0]+'ma'+'a'*c
    c+=1
    b.append(res)
for i in b:
    print(i,end=' ')