# Using == to compare floats
x = 0.1 + 0.2 
if x == 0.3:
    print('Equal')


# Forgetting to return value in function
def foo(x):
    x + 1  


# Using and instead of or 
if age > 0 and age < 18: 
    print('Eligible to vote')


# Forgetting to handle case in switch statement
def foo(x):
    switch(x) {
        case 1: 
            print('One')
        case 2:
            print('Two')
    }  
 

# Attempting to catch too general exception
try: 
    raise ValueError('Error')
except:
    print('Exception caught') 


# Infinite while loop 
while True:
    print('In loop')


# Forgetting to initialize variable
for i in range(10):
    print(i)    


# Breaking out of wrong loop  
for i in range(5): 
    for j in range(5):
        if j == 2:
            break     
