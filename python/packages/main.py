#to make matematics a package we have to give the __init__ module 
'''
import mathematics

print(mathematics)   #it will access the __init__ file by default
print(mathematics.a)
'''
'''  # method 1
from mathematics import (
    simple,
    complex
) 

print(simple.subtract(1,2))
print(complex.cube(3))
'''
'''
# method 2 
from mathematics import*
print(simple.subtract(1,2))
print(complex.cube(3))
'''

from mathematics.simple import subtract  #when the import is called of simple then the entire simple file is exexuted

print(subtract(1,2))