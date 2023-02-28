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




#######################################
# Black box vs White box TESTING
#
#######################################
# White box testing
# AKA clear box or transparent testing
# As they know how the code works
# 
# relies on the test creators knowledge of the 
# software being tested to construct the test cases
#######################################
# Black box testing
# 
# written with an awareness of what the program is supposed to do, 
# its requirements or specifications, but not how it does it
#########################################


##############################################
# INTEGRATED TESTING
#
# Everything works as whole
#
# The purpose of integrated testing is to ensure that the individual components of the software 
# system work together as expected and meet the functional and non-functional requirements of the system.
##############################################
# Regression Tests
#
# is performed to verify whether changes made to a software application, system, 
# or codebase have introduced any new defects or have inadvertently caused existing features to break or malfunction
#
# Regression testing is usually done after modifications or updates to the software to ensure that the new changes 
# have not broken any previously working features
###############################################
# Smoke Tests
#
# Running a piece of software code as-is to see if it runs
# This test finds out if the program can run in its basic form before undergoing more refined test cases.
##############################################
# Load Tests
#
# Can it handle under load
##############################################


###########################################
# Test driven development
#
# calls for creating the test before writing the code
#
##############################################


#################################
# Some practice quiz examples
#
#################################

# In what type of test is the code not transparent? Black-box test

# Verifying an automation script works well with the overall system and external entities describes what type of test? Integration test

# A test that is written after a bug has been identified in order to ensure the bug doesn't show up again later is called? Regresssion

# What type of software testing is used to verify the software’s ability to behave well under significantly stressed testing conditions? Load test



############################################
# TRY-EXCEPT Construct
#
#
############################################
# The code in the except block is only executed if one of the instructions in the try block
# raises an error of the matching type
##########################################
# Assert -  can help provide a reason an error has occurred in a function
#########################################
# Raise
#############################################

"""
print("Try except example!!!!!!!!!!!!!")

try:
    x = int(input("Please enter a number: "))
    result = 10 / x
    print("The result is:", result)
except ZeroDivisionError:
    print("You cannot divide by zero.")
except ValueError:
    print("That was not a valid number.")


In this example, the program prompts the user to enter a number, and then attempts to divide 10 by that number. 
If the user enters an invalid number (such as a string), a ValueError exception will be raised. If the user enters 0 as the number, 
a ZeroDivisionError exception will be raised.

By wrapping the code inside a try...except block, the program can handle these exceptions gracefully, without crashing. 
If either of these exceptions is raised, the corresponding except block will be executed, printing an error message to the console. 
Otherwise, if the division succeeds, the result will be printed to the console.



print("ASSERT example!!!!!!!!!")

def divide(a, b):
    assert b != 0, "Cannot divide by zero!"
    return a / b

print(divide(10, 5))   # Output: 2.0
print(divide(10, 0))   # Raises an AssertionError with message "Cannot divide by zero!"


In this example, we define a function called divide that takes two arguments, a and b, and returns the result of dividing a by b. 
Before performing the division, we use an assert statement to check that b is not zero. 
If b is zero, the assert statement will raise an AssertionError with the specified error message.

In the first call to divide, we pass in a = 10 and b = 5, which results in a valid division, so the function returns 2.0. 
In the second call, we pass in a = 10 and b = 0, which would result in a division by zero. Because of the assert statement, 
an AssertionError is raised with the message "Cannot divide by zero!".

Using assert statements can be a useful way to catch errors early in your code and ensure that your assumptions about the behavior of your program are correct.



print("RAISE example!!!!!!!!!")

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age < 18:
        print("You are not old enough to vote")
    else:
        print("You are old enough to vote")

check_age(20)   # Output: "You are old enough to vote"
check_age(-5)   # Raises a ValueError with message "Age cannot be negative"


In this example, we define a function called check_age that takes one argument, age, and checks whether the age is valid for voting. 
If the age is negative, the function raises a ValueError with the message "Age cannot be negative". 
Otherwise, if the age is less than 18, the function prints a message saying that the person is not old enough to vote. 
Finally, if the age is 18 or greater, the function prints a message saying that the person is old enough to vote.

In the first call to check_age, we pass in age = 20, which is greater than 18, so the function outputs "You are old enough to vote". 
In the second call, we pass in age = -5, which is a negative value. Because of the raise statement, a ValueError is raised with the message "Age cannot be negative".

Using the raise statement can be a useful way to explicitly handle errors in your code and provide clear error messages for users or other developers who
may encounter issues.


"""


###################################
# Testing for expected errors
#
###################################
# Assertraises
# The expected error is passed first
####################################











