def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a//b
'''
 the below statement is only true when mathematics/simple.py file is called
 because __name__ specifies the import name of the particlular module 
 so if main.py is executed the value of __name__ will be mathematics.simple
 and for mathematics/simple.py value of __name__ will be __main__
'''  
#print(__name__)
if __name__=='__main__':
    print("hello world")
    a=int(input())
    b=int(input())
    print(add(1,2))

