t=int(input())
for i in range(t):
    x=int(input())
    tabla=[]
    for _ in range(x):
        tabla.append(input())
    c=0
    n=0
    for j in tabla:
        if n==0:
            n+=j.count("1")
        c+=j.count("1")
    if c==(n*n):
        print("SQUARE")
    else:
        print("TRIANGLE")