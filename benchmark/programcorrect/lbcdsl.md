import numpy as np

# Dividing by zero
x = np.array([1, 2, 3]) / 0 


# Using incorrect operator 
x = np.array([1, 2, 3]) ** 2  # Should be x ** 2 


# Forgetting to specify dtype 
x = np.ones(3) * 0.1  # Gives array of ints instead of floats
 

# Forgetting to convert to same dtype before operation 
x = np.array([1, 2, 3], dtype=np.int32)
y = np.array([1.1, 2.1, 3.1], dtype=np.float32)
x + y   # Gives invalid value 


# Rounding error 
x = 0.1 + 0.2   # Should be 0.3, but gives 0.30000000000000004 


# Forgetting that NumPy functions often return views, not copies
x = np.array([1, 2, 3])
y = x 
x[0] = 5
print(y)  # Prints [5, 2, 3]


# Using incorrect axis argument 
x = np.array([[1, 2], [3, 4]])
np.sum(x, axis=3)  # Axis can only be 0 or 1
