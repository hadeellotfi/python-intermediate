# Local Scope 
# Let’s return to our puzzling example from the previous exercise: 

def favorite_color(): 
  color = 'Red'
 
# print(color) 

"""
In this case, the name of color is scoped locally to
 the function favorite_color(). Since the statement
   print(color) is called outside of the function, 
   it has no access to the local scope (and thus the local namespace)
     inside of favorite_color() and returns an error.

"""

# However, if we were to refactor our code: 
def favorite_color(): 
  color = 'Red'
  print(color) 
 
favorite_color() 

