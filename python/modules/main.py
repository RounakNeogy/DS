
'''
METHOD 1 

import calculator as lib     #we can make an alias this way

def calculator():
    print(1+5," its working")

print(lib.CONSTANT)
print(lib.add(1,2),end=" ")
print(lib.add(10,2),end=" ")
print(lib.add(15,2),end=" ")
print(lib.add(20,2))


a=lib.A()
print(type(a))

calculator()
'''

#METHOD 2

from calculator import (       # it imports the specified definitions
    add as addition,            # an alias
    diff as subtraction,
    a,
    b,
    c
)

print(addition(1,2))
print(subtraction(2,1))
print(a)
print(b)
print(c)


''' 
METHOD 3


from calculator import *           #it imports all definitions     but it is not recommanded

print(globals())
print(add(6,2))
print(diff(8,1))
print(a)

'''
