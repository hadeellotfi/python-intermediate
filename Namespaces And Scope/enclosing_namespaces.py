# Enclosing Namespace 
# is a special type of local namespace called the enclosing namespace. 

"""
Enclosing namespaces are created specifically when we work
 with nested functions and just like with the local namespace,
   will only exist until the function is done executing. 
   Lets take a look at an example:

"""

global_variable = 'global'
 
def outer_function():
  outer_value = "outer"
 
  def inner_function():
    inner_value = "inner"
  inner_function()
  # Added locals output
  print(locals())
 
outer_function()

# Would output:
# {'outer_value': 'outer', 'inner_function': <function outer_function.<locals>.inner_function at 0x7f46b56bc820>}