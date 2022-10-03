str=input()
s=str.split()
max=0
for i in s:
    if(len(i)>max):
        max=len(i)
print(max)