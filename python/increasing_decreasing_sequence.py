n=int(input())
a=[]
for i in range(n):
    c=int(input())
    a.append(c)
f,s,v=0,0,0
i=1
while i<len(a):
    if a[i-1]>a[i]:
        i+=1
    elif a[i-1]==a[i]:
        i+=1
        break
    else:
        break

if v==1:
    print("false")
else:
    print("true")