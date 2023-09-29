import numpy as np

# Missing parenthesis 
x = np.zeros 5 

# Extra parenthesis
x = np.zeros((5))  

# Missing bracket
x = np.zeros [5]

# Extra bracket 
x = np.zeros](5)  

# Wrong function name
x = np.zeroes(5)  

# Missing comma 
x = np.zeros(5, 2) 

# Wrong indentation
if x.shape == (5,):  
print(x.shape)

# Using = instead of == in condition
if x.shape = (5,):
   print(x.shape)

# Forgetting . in method call
x = np.random(5)   

# Forgetting to close multiline string
s = '''numpy is useful 

# Attempting to access index of 0-d array
x = np.zeros(())
x[0]