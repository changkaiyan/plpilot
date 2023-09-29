def  factorial(n):         # no space after def
   if n==1:          # no space around ==
       return 1
   else:
       return n*factorial(n-1)     # not indented properly
    

user_input = input("Enter a number: ")   # no space after =

num = int(user_input)  

result = factorial(num)
print("The factorial of",num,"is",result)   
                   # improperly spaced + and ,  
                     
words = ['hello' , 'world' ,'this' 'is' ,   # no comma after world, no space after is 
                'a' 'list' ]        

for word in words:     # not indented
   print(word)
                
if 10 > 5 :     # space missing before :
   print("10 is greater than 5")   

x = 5 
y = 10

if x > 2 and y > 8 : # space missing before :
   print("Both conditions are true")

"""This is 
   a docstring """  # space missing after """ 
    
def add(x,y):  # arguments not on separate lines
   """Adds two numbers together.
   
   Returns the sum of x and y.
   """
   
   sum = x + y
   return sum
