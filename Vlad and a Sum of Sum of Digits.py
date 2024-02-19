def digitos(y):
    c=0
    while y>0:
        c+=y%10
        y=y//10
    return c
def f (x):
    if x==1: return 1
    if x>9:
        return digitos(x)+f(x-1)
    return x+f(x-1)

t=int(input())
for _ in range(t):
    a=int(input())
    print(f(a))