import numpy as np

def calculate(a, b):  # a and b are not descriptive
    arr1 = a         # arr1 is not descriptive
    arr2 = b         # arr2 is not descriptive
    
    total = np.sum(arr1) # total is not descriptive
    prod = np.prod(arr1) # prod is not descriptive
    diff = np.subtract(arr1, arr2) # diff is not descriptive
    div = np.divide(arr1, arr2)   # div is not descriptive
    
    return total, prod, diff, div

data = np.random.rand(5, 3)   # data is not descriptive
tmp_arr = np.zeros((2, 4))   # tmp_arr is not descriptive

_arr = np.ones(10)           # does not follow convention
Arr = np.linspace(0, 10, 5)  # not snake_case

res1 = calculate(data, tmp_arr) 
result2 = calculate(Arr, _arr)   # result2 is not descriptive 

my_string = "Hello"          # good
str1 = "Hi"                   # str1 is not descriptive

print(my_string, str1, Arr, _arr, tmp_arr)  
print(res1, result2)