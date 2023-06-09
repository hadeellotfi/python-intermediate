# Python Intermediate Learning Course Summary 
In Learn Intermediate Python 3, I learned how to leverage Python’s unique features and techniques to build powerful, sophisticated applications. and how to expedite my data processing and management, manage my resources, test my code using the Unittest testing framework, and more. Here’s an overview of the courses modules:

* Functions Deep Dive
* Object-Oriented Programming
* Iterators & Generators
* Specialized Collections
* Resource Management
* Unit Testing

# Introduction
## Python Gotcha: Mutable Default Arguments 
Learn about a common Python gotcha when using mutable default arguments in functions! 

## A Python Gotcha!
When writing a function with default arguments, it can sometimes be tempting to include an empty list as a default argument to that function. 

To summarize, I learned:

* What a Python gotcha is.
* What mutable objects are in Python.
* A common gotcha that occurs when using mutable default arguments.
* A workaround for mutable default arguments by using None paired with a conditional statement.

Keep this gotcha in mind whenever deciding to use a mutable object as a default argument. While most developers recommend staying away from this approach, there are notable use cases for this syntax that may be worth looking into!

# Function Arguments
## Function Arguments: A Recap 

In Python, there are three common types of function arguments:

1. Positional arguments: arguments that are called by their position in the function definition.
2. Keyword arguments: arguments that are called by their name.
3. Default arguments: arguments that are given default values.
## Function Arguments

So far we have seen how both *args and **kwargs can be combined with standard arguments. This is useful,
 but in some cases, we may want to use all three types together! Thankfully Python allows us to do so as 
 long as we follow the correct order in our function definition. The order is as follows:

1. Standard positional arguments
2. *args
3. Standard keyword arguments
4. **kwargs

# Namespaces and Scope

## Namespaces
A namespace is a collection of names and the objects that they reference. Python will host a dictionary where the keys are the names that have been defined and the mapped values are the objects that they reference. 

Four distinct types of namespaces that Python generates:

1. Built-In
2. Global
3. Local
4. Enclosing

<img src="images/namespaces.JPG?raw=true"  width="600" height="400"/>

I’ve covered:

* Names as identifiers for objects in Python.
* What namespaces are.
* The built-in namespace and how to access it using __builtins__.
* The global namespace and how to access it using globals().
* The local namespace and how to access it using locals().
* The enclosing namespace - a special type of local namespace that occurs when working with nested functions.

## Scope 
### Introduction to Scope 

<img src="images/scope.jpg?raw=true"  width="600" height="400"/>
I’ve covered:

* The concept of scope and the LEGB rule.
* What the local scope is.
* What a nested function is and the enclosing/nonlocal scope.
* What the global scope is.
* How to modify behavior using the global statement.
* How to modify behavior using the nonlocal statement.

# Functions Deep Dive
## Lambda Functions 

