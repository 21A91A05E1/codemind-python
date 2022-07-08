str=input()
s=0
for i in str:
    if i in '0123456789':
        s=s+int(i)
print(s)