# Local Namespace 

"""
Now that we have examined the built-in and global namespaces,
 lets dive into the deepest level of namespaces - the local namespace. 
 To do so, lets start by examining this program:

"""
global_variable = 'global'
 
def add(num1, num2):
  nested_value = 'Inside Function'   
  print(num1 + num2)
  print(locals())

add(5, 10)  

# Would output: 
15
{'num1': 5, 'num2': 10, 'nested_value': 'Inside Function'} 

"""
We called locals() inside the add() function to get the local namespace
 generated when the function is executed. If we called locals() outside
   of a function in our program, it behaves the same as globals().

The value printed from calling locals() represents the namespace
 that only exists inside of the function. Notice even the function
   parameters num1 and num2 exist alongside the variable name nested_value.
     The namespace does not include global_variable since it exists outside
       of the function (in the global namespace).
"""

# example 
global_variable = 'global'



print(' -- Local and global Namespaces with empty script -- \n')
# Write Checkpoint 1 here:
print(locals())
print(globals())

# Write Checkpoint 2 here:
def divide(num1, num2):
  result = num1/ num2
  print(locals()) 

# Write Checkpoint 3 here:
def multiply(num1, num2):
  product = num1 * num2 
  print(locals()) 


print(' \n -- Local Namespace for divide -- \n')
# Write Checkpoint 4 here:
divide(3, 4)

print(' \n -- Local Namespace for multiply -- \n')
# Write Checkpoint 5 here:
multiply(4, 50)

print(' \n -- Local Namespace final -- \n')
# Write Checkpoint 6 here:
print(locals()) 

# output 
"""

Output:
 -- Local and global Namespaces with empty script -- 

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7ff1e6f7cc18>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'script.py', '__cached__': None, 'global_variable': 'global'}
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7ff1e6f7cc18>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'script.py', '__cached__': None, 'global_variable': 'global'}
 
 -- Local Namespace for divide -- 

{'result': 0.75, 'num2': 4, 'num1': 3}
 
 -- Local Namespace for multiply -- 

{'product': 200, 'num2': 50, 'num1': 4}
 
 -- Local Namespace final -- 

{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7ff1e6f7cc18>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'script.py', '__cached__': None, 'global_variable': 'global', 'divide': <function divide at 0x7ff1e6fa3e18>, 'multiply': <function multiply at 0x7ff1e6d9dd08>}



"""






