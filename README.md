# proator (The python PROtotype validATOR) 
Python function prototyping and call time check.
Validates/restricts the input parameter types of any python function.

#How to install Proator using pip:
```
$ pip install proator
```
#Source code sample to use Proator:
```python
import types

from proator.function_prototype import ovrprototype
from proator.function_prototype import prototype

@prototype(types.IntType)
def foo1(a):
    print "done"
    pass

@prototype(types.BooleanType, types.BooleanType)
def foo2(a, b):
    print "done"
    pass

@ovrprototype([types.BooleanType, types.IntType])
def bar1(a):
    print "done"
    pass

@ovrprototype(
    [types.StringType, types.IntType],   # parameter types for a
    [types.IntType])                     # parameter type for b
def bar2(a, b):
    print "done"
    pass

if __name__ == '__main__':
    # single type for one feild.
    foo1(True)
    foo1(1)
    foo1("Hello")         # This will fail as input parameter type is mismatched.
    foo2(True, False)     # Boolean, Boolean is allowed 
    foo2(True, "xyz")     # This will fail as input parameter type is mismatched.
    foo2(True)            # This will fail as mismatch in number of arguments.
    
    # multiple type for one feild.
    bar1(1)               # integer is allowed
    bar1(True)            # boolean is allowed
    bar1("xyz")           # This will fail as input parameter type is mismatched.
    bar2(5, 5)            # integer, integer is allowed 
    bar2("Hello", 5)      # string , integer is allowed
    bar2(5, "Hello")      # not allowed, will fails because integer, string is not allowed.
```
