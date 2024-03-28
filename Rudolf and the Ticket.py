for _ in range(int(input())):
    e = list(map(int,input().split()))
    l = list(map(int,input().split()))
    r = list(map(int,input().split()))
    if (max(l)+max(r))<=e[2]:
        print(e[0]*e[1])
        continue
    while True:
        if e[0]==0 or e[1]==0: break
        if max(l)>=e[2]:
            e[0]-=1
            l.remove(max(l))
        elif max(r)>=e[2]:
            e[1]-=1
            r.remove(max(r))
        else: break
    if e[0]==0 or e[1]==0: 
        print(0)
        continue
    c=0
    for i in l:
        for j in r:
            if i+j<=e[2]:c+=1
    print(c)