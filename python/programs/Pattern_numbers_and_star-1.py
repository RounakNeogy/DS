n=int(input())
g=1
for i in range(n):
    for j in range(n-i):
        print(j+1,end=' ')
    if i!=0:
        for k in range(g):
            print("*",end=' ')
        g=g+2
    print("\n")
