#################################################
# Code Testing
#
#
#################################################
# Unit testing, integration testing, automated testing, and sanity testing are all different types of software testing that are performed during 
# the software development life cycle to ensure that the software functions as intended.
#
# Unit Testing: Unit testing is the process of testing individual components or units of code in isolation to ensure that they are working as intended. 
# It involves writing test cases for each unit and running them to ensure that the unit functions as expected.
#
# Integration Testing: Integration testing is the process of testing how different units or components of the software work together. 
# It involves testing the interactions between these units to ensure that they are working as expected.
#
# Automated Testing: Automated testing is the process of using software tools to run test cases automatically. 
# It involves writing test scripts that can be run automatically, without the need for manual intervention.
#
# Sanity Testing: Sanity testing is a type of testing that is performed to ensure that the most important and critical functions of the software are working 
# as expected after a new build or release. It is a quick and simple test that helps to identify major issues before more comprehensive testing is performed.


##############################
# Unit testing (isolation)
##############################
# The most common type and used to verify that small, isolated parts of a program or correct
# Unit tests are generally written alongside the code to test the behavior of individual pieces or units like functions or methods. 
# Unit tests help assure the developer that each piece of code does what it's meant to do.

## Writing unit tests in python #################
# The convention is to call the script with the same name of the module that it's testing and appending the suffix _test.
#
# Python provides a module called unittest
# This module includes a number of classes and methods that let us easily create unit tests for our code.

# Understand some basic assertions when comparing
#
# assertEqual(a, b)  checks a==b
# assertNotEqual(a, b)  checks a!=b
# assertTrue(x)   checks bool(x) is true
# assertFalse(x)  checks bool(x) is False



print("Example 1")
import unittest

def add_numbers(a, b):
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-2, -3), -5)

    def test_add_zero_numbers(self):
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == '__main__':
    unittest.main()




# In this example, we have a function add_numbers that takes two numbers as input and returns their sum. 
# We also have a test class TestAddNumbers that inherits from unittest.TestCase.

# Inside the test class, we define three test methods:
#
# test_add_positive_numbers tests that adding two positive numbers returns the expected sum.
# test_add_negative_numbers tests that adding two negative numbers returns the expected sum.
# test_add_zero_numbers tests that adding zero to zero returns zero.
# Each test method uses an assertion to check that the output of the add_numbers function is equal to the expected result.

# Finally, we use unittest.main() to run the tests. When we run this script, unittest will execute all the test methods 
# in TestAddNumbers and report whether they passed or failed.


"""
print("Example 2")

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

"""



### Edge cases #############
# Edge cases are inputs to our code that produce unexpected results, and are found at the extreme ends of the ranges of input we imagine our programs will typically 
# work with. 
# Edge cases usually need special handling in scripts in order for the code to continue to behave correctly

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b






