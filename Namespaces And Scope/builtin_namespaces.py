# Built-in Namespace 
# One of the four main types of namespaces that exist in Python is the built-in namespace. 

"""
Ever wonder why functions like print() and str() are available
 to us in all our programs? Well, Python knows these function names
   because they exist in the highest level of namespaces and thus can
     be called in any program we write.

Whenever we run a Python application, we are provided a built-in namespace 
that is created when the interpreter is started and has a lifetime until 
the interpreter terminates (usually when our program is finished running). 
Since Python provides the namespace, these objects are accessible without 
the need to import a separate module.

Lets take a look together at the standard built-in namespace! In order to see it,
 we can use the following statement:

"""
print(dir(__builtins__)) 

# This allows us to access the builtins module that Python provides for us. 
# Our output would give us:

['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']

# Wow! That’s a bit overwhelming. 
# Let’s note a few interesting facts about the objects hosted built-in namespace:

"""
1. It contains many of the built-in functions we are able to use in our Python programs
  such as str(), zip(), slice(), sorted(), and many more.
2. It also hosts many of the exceptions that we may encounter in our programs such as
 'ArithmeticError', 'IndexError', 'KeyError', and many more.
3. There are even constants like True and False!

"""

print(dir(__builtins__))
