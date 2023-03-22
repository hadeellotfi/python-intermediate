# NAMESPACES 
# Introduction to Names and Namespaces 
"""
In Python, a name (sometimes also called a symbolic name) is an identifier for an object.
 In the programs we have written so far, we have been using the concept of naming all
   along! Lets take a look at an example:
"""
color = "cyan" 

# Here, we assign color as the name of the string "cyan". 

'''
Python uses the system of names so that it can differentiate between each distinct
 object (such as a string or a function) that we define. In most programs, 
 Python has to keep track of the hundreds and sometimes even thousands of names.
   So, how exactly does Python store all of this information? Well, it creates what 
   is called a namespace.

A namespace is a collection of names and the objects that they reference.
 Python will host a dictionary where the keys are the names that have been 
 defined and the mapped values are the objects that they reference.

'''

# In the example above, the namespace Python creates would look something like this: 
{'color': 'cyan'} 

# So, in this case, if we tried to print the variable color: 
print(color) 

"""
Python would search the namespace defined above for a key named color and 
provide the value to be run in our program. Thus we would see the output of 'cyan'.
In the next exercises we will explore the four distinct types of namespaces that Python generates: 
1. Built-In
2. Global
3. Local
4. Enclosing

"""
