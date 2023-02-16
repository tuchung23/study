###################################
# REGULAR EXPRESSIONS
# 
#
###################################
# re Module allows us to search
# pnemonic = stands for regular expressions
#
# USE REGEXP101.com whilst building it to find the matches
# It's the best!!!!
###################################
# re.search()  ; searches for the first occurrence of a pattern in a string and returns a match
# re.findall() ; finds all instances
####################################

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
  # remember [] contain OR , () is the string itself
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

# use regex101.com  to build   ; enter into test string all the times and try to match left to right
# must start between 1 and 12 inclusive ;  cannot use 12 as it sees it as 2 chars  ;  ^[1-12]
#  ^(1[0-2]|[1-9])  ; this matches at the start 10,11,12 (double digits) OR range from 1-9
# to match 00 and 59 inclusive ; first number between 0-5 ; second between 0 and 9 ; deal one letter at a time
# optional space ; \s  matches space , use * for zero or more meaning optional first
# end in am or AM , pm or PM


import re
def check_time(text):
  pattern = r"^(1[0-2]|[1-9]):[0-5][0-9]\s*(am|AM|pm|PM)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False


# Question 3
# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses, 
# with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. 
# For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since (IM) 
# satisfies the match conditions." Fill in the regular expression in this function: 

print("Practice Question 3")

# search for a first (  ;  Have to escape the special char by using \(
# first letter after ( found can be a number or must be a capital ; [A-Z0-9]
# 2nd must have one or more [0-9a-zA-Z]+
# end with a )

import re
def contains_acronym(text):
  pattern = r"\([A-Z0-9][0-9a-zA-Z]+\)" 
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True


# Question 4
# Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits, and sometimes, but not always, 
# followed by a dash with 4 more digits. The zip code needs to be preceded by at least one space, and cannot be at the start of the text.

print("Practice Question 4")

# must have 5 individual digits so no greedy chars here and can have a "-" after
# cannot be at the start
# needs to have a space before it ,  \s+

import re
def check_zip_code (text):
  result = re.search(r"\s+\d{5}\s*\-*(\d{4}|\s*)", text)
  return result != None

# \s matches any whitepspace
# \d matches a digit (equivalent to [0-9])
# {5} matches the previous token exactly 5 times
# \s* matches any whitespace 0 or more times , meaning optional whitespace
# \-  matches -  0 or more times , meaning it is optional if its there
# (\d{4}|\s*)    ; this means match the 4 extra digits OR it's 0 or more whitspace

#  use * is good for optional and | for OR



print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False



##############################################
# Capturing groups
#
# Portions of the pattern that are enclosed in parentheses
##############################################

result=re.search(r"^(\w*), (\w*)$" , "Lovelace, Ada")
print(result)
# returns <re.Match object; span=(0, 13), match='Lovelace, Ada'>

print(result.groups())
# returns tuple ('Lovelace', 'Ada')


###### More on Repetition qualifiers ########################
#
# Curly braces ({}) - allow you to specify a specific number of occurrences of the preceding character or group of characters.

# r"[a-zA-Z]{5}"  -> this matches 5 letter words like 'ghost'

# re.findall()   -> find all instances

# abc{2}      matches a string that has ab followed by 2 c
# abc{2,}     matches a string that has ab followed by 2 or more c
# abc{2,5}    matches a string that has ab followed by 2 up to 5 c
# a(bc)*      matches a string that has a followed by zero or more copies of the sequence bc
# a(bc){2,5}  matches a string that has a followed by 2 up to 5 copies of the sequence bc



