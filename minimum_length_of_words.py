str=input()
str=str.split()
min=100
for i in str:
    if(len(i)<min):
        min=len(i)
print(min)