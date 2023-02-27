###############################################
# JUPYTER Lab
#
###############################################
print("Jupyter LAB")

import re 
  
my_txt = "An investment in knowledge pays the best interest."
#my_txt="The best preparation for tomorrow is doing your best today."


def LetterCompiler(txt):
    # returns a list of string matches
    result = re.findall(r'([a-c])', txt)
    return result

print(LetterCompiler(my_txt))




import unittest

# note this class format
class TestCompiler(unittest.TestCase):

    def test_basic(self):
        testcase = "The best preparation for tomorrow is doing your best today."
        expected = ['b', 'a', 'a', 'b', 'a']
        self.assertEqual(LetterCompiler(testcase), expected)


class TestCompiler2(unittest.TestCase):
    
    def test_two(self):
        testcase = "A b c d e f g h i j k l m n o q r s t u v w x y z"
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

# EDGE CASES HERE
    def test_three(self):
        testcase = "Abcdef "
        expected = ['b', 'c']
        self.assertEqual(LetterCompiler(testcase), expected)

unittest.main(argv = ['first-arg-is-ignored'], exit = False)


"""
If no issues , will return:
Jupyter LAB
['a', 'b']
...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK


###########################
But if I add wrong expected values in test_three, will return

=====================================================================
FAIL: test_three (__main__.TestCompiler2)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "c:/Github/COURSERA/Course2_JUPYTER_LAB.py", line 46, in test_three
    self.assertEqual(LetterCompiler(testcase), expected)
AssertionError: Lists differ: ['b', 'c'] != ['b', 'd']

First differing element 1:
'c'
'd'

- ['b', 'c']
?        ^

+ ['b', 'd']
?        ^


----------------------------------------------------------------------
Ran 3 tests in 0.003s

FAILED (failures=1)

"""

