# Enclosing/Nonlocal Scope 
"""
Similar to how nested functions form a unique namespace
within their enclosing functions (the enclosing namespace),
there also exist special rules that apply for accessing 
nested values. These rules make up the enclosing scope
(also known as nonlocal scope).

"""

# Let’s take a look at a nested function to see the scope in action:
def outer_function():
  enclosing_value = 'Enclosing Value'
 
  def nested_function():
    nested_value = 'Nested Value'
    print(enclosing_value)
 
  nested_function()
 
outer_function()

# Our output would be: 
# Enclosing Value 

"""
Enclosing scope allows any value defined in an enclosing function
to be accessed in nested functions below it. We can observe this
scope since nested_function() can access a variable defined one
level above in the enclosing function (outer_function()).

"""

def outer_function():
  enclosing_value = 'Enclosing Value'
 
  def nested_function():
    nested_value = 'Nested Value'
 
    def second_nested():
       print(enclosing_value)
       print(nested_value)
 
     #second_nested() 
 
  nested_function()
 
outer_function()

# Would output: 
# Enclosing Value
# Nested Value


# Modifying Scope Behavior: global Statement 
# Sometimes, we want to modify a global name from within a local scope. How do we go about doing this? 

global_var = 10
 
def some_function():
  global_var = 20
 
some_function()
 
print(global_var)


# using global 
global_var = 10
 
def some_function():
  global global_var
  global_var = 20
 
some_function()
 
print(global_var)  

""" 
In addition, the global statement can be used even if the name has not been
 defined in the global namespace. Using the global statement would create the
  new variable in the global namespace.

"""

def some_function():
  global x
  x = 30
 
some_function()
print(x)

""" 
In summary, the global keyword is used within a local scope to associate a variable
 name with a name in the global namespace. This association is only valid within the
  local scope when global is used.
  
"""


