for _ in range(int(input())):
    x=list(map(int,input().split()))
    if x[1]<=x[0] or x[1]==x[2]: print("NONE")
    elif x[1]>x[2]: print("PEAK")
    else: print("STAIR")