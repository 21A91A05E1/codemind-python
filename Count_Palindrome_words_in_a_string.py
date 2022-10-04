s=input().split()
c=0
for i in range(len(s)):
    if(s[i].lower()==s[i].lower()[::-1]):
        c+=1
print(c)