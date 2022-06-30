n=input()
a=[]
for i in n:
    if(int(i)%2==0):
        continue
    else:
        a.append(int(i)**2)
for i in a:
    print(i,end='')