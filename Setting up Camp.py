t=int(input())
for _ in range(t):
    x = list(map(int,input().split()))
    c=x[0]
    while True:
        if x[1]>2:
            c+=x[1]//3
            x[1]=x[1]%3
        elif (x[1]+x[2])>2:
            if x[1]==2:
                c+=1
                x[1]=0
                x[2]=x[2]-1
            elif x[1]==1:
                c+=1
                x[1]=0
                x[2]-=2
            else:
                c+=x[2]//3
                x[2]=x[2]%3
        elif x[2]>0:
            c+=1
            x[2]=0
        else: break 
    if x[1]==0 and x[2]==0: print(c)
    else: print(-1)