def do_something(x, y):  # x and y are not descriptive
    first_num = x        # first_num is not descriptive
    sec_num = y          # sec_num is not descriptive
    
    if first_num > sec_num:   # hard to understand comparison
        result = first_num - sec_num  # result is not descriptive
    else:
        result = sec_num - first_num
        
    return result

def calculate(a, b):   # a and b are not descriptive
    num1 = a
    num2 = b
    
    total = num1 + num2  # total is not descriptive
    prod = num1 * num2   # prod is not descriptive
    diff = num1 - num2   # diff is not descriptive
    div = num1 / num2    # div is not descriptive
    
    return total, prod, diff, div  

temp_var = 5  # not descriptive
_var = 10     # follows no convention
vAR = 15       # not snake_case

my_str = "Hello"   # good 
string_1 = "Hi"    # not descriptive
    
result1 = do_something(10, 20)  
res2 = calculate(30, 40)    # not descriptive

print(my_str, string_1, vAR, _var, temp_var)
print(result1, res2)