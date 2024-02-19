t=int(input())
for _ in range(t):
    a=tuple(map(int,input().split()))
    b=tuple(range(1,a[0]+1))
    c1=()
    c2=()
    c3=()
    c4=()
    r=()
    for i in range(1,a[0]+1):
        if i%2!=0:
            c1+=(i,)
        elif i%2!=0 and (i*2 in b):
            c2+=(i*2,)
        elif i%2!=0 and (i*3 in b):
            c3+=(i,)
        else:
            c4+=(i,)
    r=c1+c2+c3+c4
    print(r[a[1]-1])