import numpy as np    # imports in the middle of the code

def foo(x):        # no space after def
     if x==5:     # no space around ==
          print(x)   # inconsistent indentation
     elif x>10:    # no space after elif
         bar(x)   # inconsistent indentation
     else:
         print("Invalid input")  # inconsistent indentation
         
def bar(y):        # no space after def
       return y*2   # inconsistent indentation
  
x = 10               # variable defined at random place
  
z = np.zeros(5)      # another import in the middle
                   # blank line has too much space  
                    
foo(x+z[1])            # brackets not on same line   

if x > 5: # space missing before colon
         print(x)
# blank comment line
                  
"""This is 
   a multiline  
              docstring"""    # inconsistent indentation in docstring