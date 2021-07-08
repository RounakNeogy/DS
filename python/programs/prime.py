import math
a=int(input())
f=0
g=int(math.sqrt(a))
for i in range(2,g+1):
    if a%i==0:
        f=1
        break     
if f==1:
    print("Not Prime")
else:
    print("Prime")