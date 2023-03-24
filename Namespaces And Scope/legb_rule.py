# Scope Resolution: The LEGB Rule
""" 
While most of our focus so far has been around where we can access namespaces, 
to truly get a full picture of scoping rules, we must also examine how Python 
handles scope resolution.

Scope resolution is a term used to describe a search procedure for a name in
the various namespaces. A set of rules dictates the order 
that the search needs to follow.

In Python, the unofficial rule (often referred to in literature but does
not exist in the official documentation) is known as the LEGB rule.

LEGB stands for Local, Enclosing, Global, and Built-in. These four letters 
represent the order of namespaces Python will check to see if a name exists.

"""
