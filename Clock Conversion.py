for _ in range(int(input())):
    r=input().split(":")
    
    if int(r[0])>=12:
        p=int(r[0])-12
        if r[0]=="12": print(f"12:{r[1]} PM")
        elif p>9: print(f"{p}:{r[1]} PM")
        else: print(f"0{p}:{r[1]} PM")
    else: 
        if r[0]=="00": print(f"12:{r[1]} AM")
        else: print(f"{r[0]}:{r[1]} AM")