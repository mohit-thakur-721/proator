# proator
Python function prototyping and call time check.

#Sample code to use Proator.

import types

from proator.function_prototype import ovrprototype
from proator.function_prototype import prototype


@prototype(types.IntType)
def test_syntax1(a):
    print "done"
    pass

#@ovrprototype([types.BooleanType, types.IntType])
def test_syntax2(a):
    print "done"
    pass

#@prototype(types.BooleanType, types.BooleanType)
def test_syntax3(a, b):
    print "done"
    pass

@ovrprototype(
    [types.BooleanType, types.IntType], 
    [types.IntType])

def test_syntax4(a, b):
    print "done"
    pass



if __name__ == '__main__':
    # single type for one feild.
    test_syntax1(True)
    test_syntax1(1)
    test_syntax1("Hello")    # This will fail as input parameter type is mismatched.
    
	# multiple type for one feild.
    test_syntax2(1)
    test_syntax2(True)
    test_syntax3(True, False)
    test_syntax4(5, False)
    test_syntax4(True, 7)
