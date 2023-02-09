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

# $ (dollar): Matches the end of a line or string.

# * (asterisk): Matches zero or more occurrences of the preceding character or group.

# + (plus): Matches one or more occurrences of the preceding character or group.

# ? (question mark): Matches zero or one occurrence of the preceding character or group.

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








