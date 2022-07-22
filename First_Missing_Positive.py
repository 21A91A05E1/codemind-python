n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(1,max(a)+1):
    if i not in a:
        print(i) 
        c+=1
        break
if c==0:
    print(max(a)+1)