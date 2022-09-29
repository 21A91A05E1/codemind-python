n=int(input())
for i in range(n):
    t=int(input())
    for i in range(0,n):
        for j in range(t-1,1,-1):
            c=0
            for k in range(1,j+1):
                if j%k==0:
                    c+=1
            if(c==2):
                bp=j
                a=t-bp
                break
        for j in range(t,t+50):
            c=0
            for k in range(1,j+1):
                if j%k==0:
                    c+=1
            if(c==2):
                ap=j
                b=ap-t
                break
    if(a<=b):
        print(bp)
    else:
        print(ap)