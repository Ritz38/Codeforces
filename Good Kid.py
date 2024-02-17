t=int(input())
for i in range(t):
    n=int(input())
    a=tuple(map(int,input().split()))
    a=a[:a.index(min(a)):]+(min(a)+1,)+a[a.index(min(a))+1::]
    r=1
    for j in range(n):
        r*=a[j]
    print(r)