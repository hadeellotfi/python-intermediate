# FUNCTION ARGUMENTS 
# Variable number of arguments: *args 
"""
To start exploring variable argument lengths in Python functions, 
lets take a look at a familiar function we have been using for a long time:

"""
print('This', 'is', 'the', 'print', 'function') 

"""
Notice how the print() function does not care how many
 arguments we pass to it. It has no expectation that 
 we are going to pass in one argument or even a million! 
 So the question is, how does print() accomplish this?

Well, in Python, there is an additional operator called the unpacking operator (*).
 The unpacking operator allows us to give our functions a variable number of 
 arguments by performing whats known as positional argument packing

 Lets explore how it works by examining a basic 
 function that utilizes the unpacking operator:

"""

def my_function(*args):
  print(args)

# If we called this function with random arguments: 
my_function('Arg1', 245, False) 

# Our output would show us what is inside of *args:
('Arg1', 245, False) 


# Variable number of arguments: **kwargs 
"""
Python doesnt stop at allowing us to accept unlimited positional arguments;
 it also gives us the power to define functions with unlimited keyword arguments.
   The syntax is very similar but uses two asterisks ** instead of one. 
   We typically call these kwargs as a shorthand for keyword arguments.

"""
# Let’s examine a function that prints out some useful information about kwargs to see it in action: 

def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an 'anything_goes' keyword arg and print it
  print(kwargs.get('anything_goes'))
 
arbitrary_keyword_args(this_arg='wowzers', anything_goes=101)

# We can observe two things: 
"""
1. **kwargs takes the form of a dictionary with all the keyword argument
   values passed to arbitrary_keyword_args. Since **kwargs is a dictionary,
   we can use standard dictionary functions like .get() to retrieve values.

2. Just as we saw with *args, the name of kwargs is completely arbitrary,
   and this example works exactly the same with the name becoming data:

"""

def arbitrary_keyword_args(**data):
  pass

# Working with **kwargs
"""
Working with **kwargs looks very similar to its *args counterpart. 
Since ** generates a standard dictionary, 
we can use iteration just like we did earlier by taking advantage of the .
values() method. Here is an example:

"""
def print_data(**data):
  for arg in data.values():
    print(arg)
 
print_data(a='arg1', b=True, c=100)

# Python requires that all positional arguments come first in our function definition. Let’s examine how this works: 
def print_data(positional_arg, **data):
  print(positional_arg)
  for arg in data.values():
    print(arg)
 
print_data('position 1', a='arg1', b=True, c=100)

# If we were to switch the position of positional_arg to come after **data, we would be met with a SyntaxError. 

# All together now!
"""
So far we have seen how both *args and **kwargs can be combined with standard arguments. This is useful,
 but in some cases, we may want to use all three types together! Thankfully Python allows us to do so as 
 long as we follow the correct order in our function definition. The order is as follows:

1. Standard positional arguments
2. *args
3. Standard keyword arguments
4. **kwargs

As an example, this is what our function definition might look like 
if we wanted a function that printed animals utilizing all three types:

"""
def print_animals(animal1, animal2, *args, animal4, **kwargs):
  print(animal1, animal2)
  print(args)
  print(animal4)
  print(kwargs)

print_animals('Snake', 'Fish', 'Guinea Pig', 'Owl', animal4='Cat', animal5='Dog')  