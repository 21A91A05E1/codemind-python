import math
t=int(input())
for i in range(t):
    n=int(input())
    s=math.sqrt(n)
    if(int(s)**2==n):
        print('True')
    else:
        print('False')