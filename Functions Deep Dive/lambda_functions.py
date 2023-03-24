# Lambda Functions
# Learn how to define a Python function in one line!

""" 
In Python, a lambda function (also commonly called an anonymous function)
is a one-line shorthand for function. Lets start by examining how lambda
functions compare to the normal functions we have already been writing.

"""
# Take for example, a function called add_two():

def add_two(my_input):
  return my_input + 2

# The same function could be written as a lambda function:

add_two = lambda my_input : my_input+2 

# So this code using the above lambda function:

print(add_two(3))
print(add_two(100))
print(add_two(-2))

# Would output: 
5
102
0

# Let’s break this syntax down: 
"""
1. The function is stored in a variable called add_two.
2. The lambda keyword declares that this is a lambda function (similar to how we use def to declare a normal function).
3. my_input is a parameter used to hold the value passed to add_two.
4. In the lambda function version, we are returning my_input + 2 without the use of a return keyword (the normal Python function explicitly uses the keyword return).

"""

# Which of the following is a proper conversion of the function below into a lambda function?
def add_bang(sentence):
  print(sentence + '!')

add_bang = lambda sentence : print(sentence + '!')

# We can do this using a conditional if statement in a lambda function, with syntax that looks like this: 
check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.' 


