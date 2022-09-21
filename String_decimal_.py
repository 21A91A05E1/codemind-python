t=int(input())
for i in range(t):
    c=0
    str=input()
    for j in str:
        if j in '0123456789':
            c+=1
    if(c==len(str)):
        print('True')
    else:
        print('False')