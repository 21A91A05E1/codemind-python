import math
n=int(input())
for i in range(0,n):
    if(n>=(2**i)):
        min=i
    if(n<(2**i)):
        max=i
        break
if(n-(2**min)<=(2**max)-n):
    print(n-(2**min))
else:
    print((2**max)-n)
        