#################################
# Reading DATA Interactively
#
##################################
# using "input"
#
#####################################

# name=input("Please enter your name: ")
# print("Hello, " + name)


##### I/O streams ##################
# The basic mechanims for performing input and output operations in your programs
# STDIN : standard input
# STDOUT : standard output
# STDERR : standard error

# data=input("This will come from STDIN: ")
# print("Now we write it to STDOUT: " + data)
# print("Now we generate an error to STDERR: " + data + 1)

##### Environment Variables ################
# Python programs get executed inside a shell command line env
# The variables set in that env are another source of information that we can use in our scripts

## Define a variable
# export FRUIT=Pineapple

## Command line arguments
# The list of arguments are stored in the sys module

## exit status/return code
# The value returned by a program to the shell
# 0 = success
# $? returns the last exit code

"""
import os
import sys

filename=sys.argv[1]

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("New file created\n")
else:
    print("Error, the file {} already exists!".format(filename))
    sys.exit(1)

""" 


