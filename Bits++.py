t=int(input())
n=0
for i in range(t):
    s=input()
    if(s[0]=='+' or s[1]=='+'):
        n+=1
    else:
        n-=1
print(n)