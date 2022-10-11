s=input()
n=int(input())
c=0
for i in s:
    if i=='a':
        c+=1
l=n//len(s)
count=l*c
k=n%len(s)
for i in range(k):
    if s[i]=='a':
        count+=1
print(count)