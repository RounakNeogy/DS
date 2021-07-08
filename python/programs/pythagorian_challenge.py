import math
t=int(input())
while t>0:
    A=int(input())
    root=math.sqrt(A)
    root_A=int(root)
    for s in range(root_A+1):
        for e in range(root_A+1):
            if s**2+e**2==A and s<=e:
                print(f"({s},{e})",end=' ')
    print("\n")
    t-=1


