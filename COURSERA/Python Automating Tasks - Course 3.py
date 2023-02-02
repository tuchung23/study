####################
# Modules
#
#####################
# On Windows
# Install the following packages whilst OFF VPN:
#
# python -m pip install pandas
#
# python -m pip install pantab
#
# python -m pip install tableauhyperapi
#
# python -m pip install tableauserverclient
#
#
# List ALL installed packages:
#
# python -m pip list
#
#########################
# How to get Python, PIP working on VPN
##########################
# https://confluence.iag.com.au/display/CYS/Netskope+Proxy+Application+configuration+guides+for+developers
# https://confluence.iag.com.au/display/CYS/Python    -> using Python and netskope
#
# As of 2/2/23 , the below commands worked beautifully whilst on vpn
# python -m pip install --trusted-host pypi.python.org --trusted-host pypi.org --trusted-host files.pythonhosted.org  pandas
# python -m pip list                  
##########################


# Interpreted Languages include:
# Python, Ruby, Javascript, Bash, Powershell
# Interpreted languages trade off slightly slower runtime performance—removing the need for compiling—by using programs called interpreters to execute the code.

# You can run a python script via
# $ python script.py   OR
# ./script.py     if the script contains the python SHEBANG #!/usr/bin/env python     


########################
# Managing files with python
#
########################

# A "File Descriptor" is a token, generated by the OS, that allows programs to do more operations with the file

############ Open and read a file contents##########################
# read only mode is the default so no need to specify
file=open("c:\\temp\\Friends.txt")
# The readline() method reads a single line from the current position, the read() method reads from the current position until the end of the file.
print(file.readline())

# Read from the current position to the end of the file
print(file.read())

# close the file which is good practice
# this unlocks the file 
# using a WITH block automatically closes the file for us
file.close()

## Iterating through files########
# with opens and closes files for us
# make file contents upper case
with open("c:\\temp\\Friends.txt") as file:
    for line in file:
        # the strip() command is used to remove extra whitespace.
        print(line.strip().upper())



## Read file contents into a LIST ##
file=open("c:\\temp\\Friends.txt")
lines=file.readlines()
file.close()
# sort it alphabetically
lines.sort()
print(lines)

## Writing to files########
# use 'w' mode to wwrite
# use 'a' mode to append
# use 'r+' mode to read and write
# if files doesnt exist, it will be created
# if it does exist, it will be overwritten as soon as the file is opened
























