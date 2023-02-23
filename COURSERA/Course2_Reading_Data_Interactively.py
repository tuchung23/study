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
Example code:

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


##### Running System commands in Python ################
# subprocess module
#
# essentially running unix like commands
##########################################################
# The subprocess.run() method takes several arguments, some of which are:
#
# args: The command to run and its arguments, passed as a list of strings.
#
# capture_output: When set to True, will capture the standard output and standard error.
#
# text: When set to True, will return the stdout and stderr as string, otherwise as bytes.
# 
# check: a boolean value that indicates whether to check the return code of the subprocess, 
# if check is true and the return code is non-zero, then subprocess `CalledProcessError` is raised.
# timeout: A value in seconds that specifies how long to wait for the subprocess to complete before timing out.
#
# shell: A boolean value that indicates whether to run the command in a shell. This means that the command is passed as a string, and shell-specific features, 
# such as wildcard expansion and variable substitution, can be used.
#
# The subprocess.run() method also returns a CompletedProcess object, which contains the following attributes:
#
# args: The command and arguments that were run.
# returncode: The return code of the subprocess.
# stdout: The standard output of the subprocess, as a bytes object.
# stderr: The standard error of the subprocess, as a bytes object.
#


import subprocess

# subprocess.run(["date"], shell=True, check=True)
# It errors without these arguments

# run the command "ls -l" in the shell
# result = subprocess.run(["ls", "-l"], shell=True, capture_output=True, text=True)

# print the output of the command
# print(result.stdout)



#### Obtaining the output of a system command ###################
#  .returncode
#  .stdout
#  .stderr
#
# UTF- 8 ncoding is part of the Unicode standard that can transform an array of bytes into a string.

#########################
# Practice Quiz
#
#########################

# What type of object does a run function return? CompletedProcess 
# This object includes information related to the execution of a command.

# How can you change the current working directory where a command will be executed? Use the cwd parameter.

# When using the run command of the subprocess module, what parameter, when set to True, allows us to store the output of a system command?
# The capture_output parameter allows us to get and store the output of the system command we're using.

# What does the copy method of os.environ do? Creates a new dictionary of environment variables
# The copy method of os.environ makes a new copy of the dictionary containing the environment variables, making modification easier.

