# Define custom types 
class Type1: 
    def __init__(self, x):
        self.x = x

class Type2:
    def __init__(self, x):
        self.x = x 

# Type mismatch, passing Type1 argument to function expecting Type2   
def foo(t): 
    print(t.x)
foo(Type1(5))

# Type mismatch, returning Type2 from function returning Type1
def bar():
    return Type2(10)
bar()

# Access non-existent method 
t1 = Type1(5)
t1.method()

# Access protected member _x 
t1._x 

# Inherit from non-existent class
class Sub(Super): 
    pass
Sub()  

t2 = Type2(10)  
# Assign Type2 to Type1 
t1 = t2

# Attempt to access index on non-iterable type  
t2[0]