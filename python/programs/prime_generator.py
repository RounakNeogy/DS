import math 
t=int(input())
while t>0:
    a=input().split()
    m=int(a[0])
    n=int(a[1])
    for i in range(m,n+1):
        f=0
        g=int(math.sqrt(i))
        for x in range(2,g+1):
            if i%x==0:
                f=1
                break
        if f==0 and i!=1:
            print(i,end=' ')
    print('\n')
    t-=1
