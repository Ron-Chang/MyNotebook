"""
Test.describe('Basic Tests')
Test.assert_equals(seven(times(five())), 35)
Test.assert_equals(four(plus(nine())), 13)
Test.assert_equals(eight(minus(three())), 5)
Test.assert_equals(six(divided_by(two())), 3)

seven(times(five())); // must return 35
four(plus(nine())); // must return 13
eight(minus(three())); // must return 5
six(dividedBy(two())); // must return 3
Ruby:

seven(times(five)) # must return 35
four(plus(nine)) # must return 13
eight(minus(three)) # must return 5
six(divided_by(two)) # must return 3
"""
import operator

def zero():
    return 0
def one():

def two():

def three():

def four():

def five():

def six():

def seven():
    return 7

def eight():

def nine():


def plus():

def minus(x):
    return operator.sub(, x)
def times():

def divided_by():

print(seven( times( five() ) ))

print("\n".join(method for method in operator.__dir__() if "__" not in method))
