for _ in range(int(input())):
    n=int(input())
    for i in range(n):
        if i%2==0:
            for j in range(n):
                if j%2==0:
                    print("##", end="")
                else: print("..",end="")
            print("")
            for j in range(n):
                if j%2==0:
                    print("##", end="")
                else: print("..",end="")
        else:
            for j in range(n):
                if j%2==0:
                    print("..", end="")
                else: print("##",end="")
            print("")
            for j in range(n):
                if j%2==0:
                    print("..", end="")
                else: print("##",end="")
        print("")
            