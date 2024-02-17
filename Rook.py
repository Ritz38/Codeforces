t=int(input())
letras=["a","b","c","d","e","f","g","h"]
for i in range(t):
    x=input()
    for j in letras:
        if j==x[0]:
            continue
        print(j+x[1])
    
    for k in range(1,9):
        if k==int(x[1]):
            continue
        print(x[0]+str(k))