n=int(input())
for i in range(n):
    x=input()
    if len(x)>10:
        print(f"{x[0]}{len(x[1:len(x)-1:])}{x[-1]}")
    else:
        print(x)