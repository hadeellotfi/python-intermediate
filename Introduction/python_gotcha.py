# A Python Gotcha! 
"""
When writing a function with default arguments, it can sometimes be tempting to include an empty list as a default argument to that function.

Lets imagine for instance we were building an application for a school. 
We want to have a function that can generate new students and return a dictionary of the students name, age, and grades. 
Since most students enter the school without any grades, its plausible to assume we can store an empty list for the property.
Here is what our function might look like:

"""
def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }

"""
Looks good so far! 
We can create two new students based off this code (assuming they have no grades yet):

"""
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

"""
Realistically, as both Chrisley and Dallas progress in school, there should be a way for us to add new grades. 
Something like this method:

"""

def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

# Alright! Let’s give Chrisley and Dallas some grades: 
addGrade(chrisley, 90)
addGrade(dallas, 100)

#Here, we expect that the output probably would be :
#[90]
#[100]

"""

That would make sense since we want each student to have an individual grades list. 
Surprisingly (or maybe not so much), the actual output is :
[90]
[90, 100]

"""

"""
Uh oh! That doesnt look right. Why does Dallas have the 90 grade that we added to Chrisley,
when they should only have the 100 we intended to add? 
This is known as a gotcha - a counterintuitive feature of a programming language
that often leads to mistakes in programs.
Lets practice catching this gotcha and then dive a bit deeper to understand why this phenomenon occurs.

"""
# What is the output of the following code? 
def update_order(new_item, current_order=[]):
  current_order.append(new_item)
  return current_order
 
# First order, burger
order1 = update_order({'item': 'burger', 'cost': '3.50'})
 
# Second order, just a soda
order2 = update_order({'item': 'soda', 'cost': '1.50'})
 
# What's in that second order again?
print(order2)

# [{'item': 'burger', 'cost': '3.50'}, {'item': 'soda', 'cost': '1.50'}]

# Mutables and Functions
"""
To understand this gotcha, we must first establish what Python classifies as mutable.
A mutable object refers to various containers in Python that are intended to be changed. 
A list for example has append and remove operations that change the elements of the list. 
Sets and dictionaries are also two other mutable objects in Python as they can be changed on the fly.


It might be helpful to note some of the objects in Python that are not mutable 
(and therefore OK to use as default arguments). int, float, and other numbers 
cant be mutated (arithmetic operations will return a new number). 
Tuples are a kind of immutable list, and strings are also immutable since operations
that update a string will all return a completely new string.

When using a mutable in function arguments, 
its important to note the following (from the offical documentation):

Default parameter values are evaluated from left to right when the function 
definition is executed. This means that the expression is evaluated once,
when the function is defined, and that the same “pre-computed” value is used for each call.


This means that when we call a function, 
the default values we provide for parameters are only created once,
and used for each subsequent call of the function. This means our grades=[] 
from our earlier function was only created once and anytime we tried to access it,
the same list was being modified. 
We can even see that the memory id of the grades property for both students is the same (using the built-in id() function):

"""

# The ids printed will vary depending on the computer we are using. 
print(id(chrisley['grades']))
print(id(dallas['grades']))

"""
While this may seem like a bit of a headscratcher, 
and even a point of contention amongst Python enthusiasts there is one 
specific solution that helps us get around this gotcha if we ever do want to use a mutable default argument. 
Lets take a look at a solution that uses the value None to get around this gotcha.

The None Workaround

If we want an empty list as a potential default argument value, 
we can use None as a special value to indicate we did not receive anything. 
After we check whether an argument was provided, we can instantiate a new list if it wasnt.
Here is what the solution looks like for our program from earlier:

"""

def createStudent(name, age, grades=None):
  if grades is None:
    grades = []
  return {
    'name': name,
    'age': age,
    'grades': grades
  }
 
def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

# Now if we create our students again and add grades to them:
chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)
 
addGrade(chrisley, 90)
addGrade(dallas, 100)

# We would get our expected result: 
# [90]
# [100]

"""
While it may seem more cumbersome to write the if clause, 
this is one of the most common (and flexible) ways to avoid 
running into issues with mutable default arguments. 
Lets practice by refactoring the last assessment code.

"""