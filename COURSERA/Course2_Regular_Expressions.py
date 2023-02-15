###################################
# REGULAR EXPRESSIONS
# 
#
###################################
# re Module allows us to search
# pnemonic = stands for regular expressions
###################################

# Here's a simple example that uses the re.search() method to search for a pattern in a string:

import re

text = "The quick brown fox jumps over the lazy dog."

# Search for the pattern "fox" in the text
match = re.search("fox", text)

if match:
    # Print the starting and ending indices of the match
    print("Found match")
    print(match)




####  GREP ###########################
# A "." matches any character
#
# The circumflex [^] and the dollar sign [$] are anchor characters which
# specifically match the start and end of a line or string, but not necessarily the words themselves.

# Always use raw strings for regular expressions in python
# a raw string is a type of string literal that is prefixed with the letter r. 
# Raw strings are useful when you need to include backslashes (\) in your string and do not want them to be treated as escape characters.

# raw string example
file_path = r"C:\Users\John\Documents\file.txt"
print(file_path)


# Case insensitive - re.IGNORECASE
# Find all instances - re.FINDALL


# List of meta characters
# . ^ $ * + ? { } [ ] \ | ( )

# Here is a brief summary of each of the regular expression metacharacters:

# . (dot): Matches any single character except a newline character.

# ^ (caret): Matches the start of a line or string.
# eg. ^gm

# $ (dollar): Matches the end of a line or string.
# eg. com$

# * (asterisk): Matches zero or more occurrences of the preceding character or group.

# + (plus): Matches one or more occurrences of the preceding character or group.
# eg. h+

# ? (question mark): Matches zero or one occurrence of the preceding character or group.
# eg  m?

# {} (curly braces): Specify a numerical range for the number of matches.

# [] (square brackets): Matches any single character within the brackets.

# \ (backslash): Escapes the special meaning of a metacharacter.

# | (vertical bar): Matches either the expression before or the expression after the bar.

# () (parentheses): Group characters together to form a subexpression.

# Character classes are written inside square brackets and let us list the characters we want to match inside of those brackets
# [pP] , [a-z]  etc


### Escaping characters ######
# use "\"  to escape a character
#



###################################
###################################
# Great website to test regular expressions
# https://regex101.com/
#
####################################

############################
# PRACTICE QUIZ Questions
#
############################
# use https://regex101.com/ to build pattern
#############################
print("Practice Question 1")

# The check_web_address function checks if the text passed qualifies as a top-level web address, 
# meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), 
# as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level
# domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters, 
# wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.

import re
def check_web_address(text):

  # cannot contain non alpha numeric chars - first char must start with ^[a-zA-Z0-9]
  # * , + or ?  to deal with sequences
  # second char can be . but cannot be @ or /
  # + requires that at least one occurrence of the preceding expression is present in the string being matched.
  # must have one or more dots
  # must end in .com , .info , .edu , .org   - must end in (\.com|\.org|\.US )$   ; | is like and OR operator
  # 
  pattern =r"^[a-zA-Z0-9]+[a-zA-Z0-9\.\-\_]*(\.com|\.org|\.US)$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True



print("Practice Question 2")
# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero, 
# followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. 
# Fill in the regular expression to do that. How many of the concepts that you just learned can you use here?

import re
def check_time(text):
  pattern = ___
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


"""
print("Practice Question 3")
import re
def contains_acronym(text):
  pattern = ___ 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


"""

