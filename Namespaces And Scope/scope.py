# Scope 
# Introduction to Scope 

"""
Recall, in Python, namespaces are the backbone 
of how our programs are stored and retrieved. 
However, knowing about namespace mechanism isnt 
enough to explain the following behavior:

"""
def printColor():
  color = 'red'
 
# print(color) 

# If we run this code, our output would give us: 
# NameError: name 'color' is not defined 

"""
Well, this is where a concept called scope comes into play.
 Scope defines which namespaces our program will look into 
 (to check names) and in what order. While multiple namespaces
   usually exist at once, this does not mean we can access all
     of them in different parts of our program! Exploring the concept
       of scope will allow us to start recognizing when and where certain
         objects may or may not be accessed.
"""

# Similar to namespaces, there are four different levels of scope. These levels are: 
# 1. Built-in Scope (We will skip talking about this scope)
# 2. Global Scope
# 3. Enclosing Scope
# 4. Local Scope