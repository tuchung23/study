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
# use 'w' mode to write
# use 'a' mode to append
# use 'r+' mode to read and write
# if files doesnt exist, it will be created
# if it does exist, it will be overwritten as soon as the file is opened

#################
# READ and WRITE first lab exercise
# Below is my working solution
#
##################

# Practice Notebook: Reading and Writing Files

# In this exercise, we will test your knowledge of reading and writing files by playing around with some text files. 
# Let's say we have a text file containing current visitors at a hotel.  We'll call it, *guests.txt*.  
# Run the following code to create the file.  The file will automatically populate with each initial guest's first name on its own line.


####### Tip - to run specific section of code in VSCODE ############
# highlight the code
# hold SHIFT and press enter
# exit prompt by CTRL-Z plus enter



# \\ to preserve character
guests = open("c:\\temp\\guests.txt", "w")
# this creates a new file if not exists
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

# iterate the list and enter one name per line
for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

## this returns
# Bob
# Andrea
# Manuel
# Polly
# Khalid

# grab contents of the file and print to stdout
with open("c:\\temp\\guests.txt") as guests:
    for line in guests:
        print(line)



# Now suppose we want to update our file as guests check in and out.  Fill in the missing code in the following cell to add guests to the *guests.txt* file as they check in.

# define the list of new guests
new_guests = ["Sam", "Danielle", "Jacob"]

# we want to append whats already there, so use 'a' descriptor
with open("c:\\temp\\guests.txt", 'a') as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()


# now output file contents to stdout
with open("c:\\temp\\guests.txt") as guests:
    for line in guests:
        print(line)


# Now let's remove the guests that have checked out already.  There are several ways to do this, however, the method we will choose for this exercise is outlined as follows:
# 1. Open the file in "read" mode.
# 2. Iterate over each line in the file and put each guest's name into a Python list.
# 3. Open the file once again in "write" mode.
# 4. Add each guest's name in the Python list to the file one by one.

checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("c:\\temp\\guests.txt", 'r') as guests:
    for g in guests:
        temp_list.append(g.strip())

# remove the users from the checked_out list
with open("c:\\temp\\guests.txt", 'w') as guests:
    for name in temp_list:
        # this compares 2 lists to each other
        if name not in checked_out:
            guests.write(name + "\n")



with open("c:\\temp\\guests.txt") as guests:
    for line in guests:
        print(line)


# The current names in the *guests.txt* file should be:  Bob, Polly, Sam, Danielle and Jacob.

# Now let's check whether Bob and Andrea are still checked in.  
# How could we do this? We'll just read through each line in the file to see if their name is in there.  
# Run the following code to check whether Bob and Andrea are still checked in.

guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("c:\\temp\\guests.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))


# We can see that Bob is checked in while Andrea is not.  Nice work! You've learned the basics of reading and writing files in Python!


###########################
# Working with files
# moving, deleting, renaming files etc
############################

## files
import os
# os.remove("c:\\temp\\guests.txt")
# os.rename(old,new)
# os.path.exists(file)   ; check if file exists and returns true or false
# os.path.getsize(file)  ; get file size
# os.path.getmtime(file)     ; file last modified
# os.path.abspath(file)    ; returns absolute path


## directories
# os.getcwd()     current working directory
# os.mkdir("new_dir")
# os.rmdir("dir")    remove empty directory only
# os.listdir()    list folder contents
# os.chdir("new_dir")     ; change directory

# check the contents of the website directory
# whether directory or file

# dir = "website"
# for name in os.listdir(dir):
#    fullname=os.path.join(dir,name)
#    # By using os.path.join we can concatenate directories in a way that can be used with other os.path() functions.
#    if os.path.isdir(fullname):
#        print("{} is a directory".format(fullname))
#    else:
#        print("{} is a file".format(fullname))


# The create_python_script function creates a new python script in the current working directory, 
# adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. 
# Fill in the gaps to create a script called "program.py".


def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w') as file:
    file.write(comments)
    filesize = os.path.getsize(filename)
  return(filesize)

print(create_python_script("c:\\temp\\program.py"))


#######################################################
# Question 2
# The new_directory function creates a new directory inside the current working directory, then creates a new empty file inside the new directory, 
# and returns the list of files in that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 


import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  # this lists it in the current directory you run the python script from
  if os.path.isdir(directory) == False:
    os.mkdir(directory)
    
  # Create the new file inside of the new directory
  os.chdir(directory)
  
  # now create a new empty file inside the new directory
  with open (filename, "w") as file:
    file.write(filename)
    #pass
  
  # Return the list of files in the new directory in a LIST
  return os.listdir()

print(new_directory("PythonPrograms", "script.py"))


#####################################################################
# Question 3
# The parent_directory function returns the name of the directory that's located just above the current working directory. 
# Remember that '..' is a relative path alias that means "go up to the parent directory". Fill in the gaps to complete this function.

# example
# directory = '/path/to/dir'
# filename = 'example.txt'
# file_path = os.path.join(directory, filename)
# RETURNS:  /path/to/dir/example.txt


current_dir = os.getcwd()
# os.path.dirname returns the directory name of pathname path , essentially the parent
parent_dir = os.path.dirname(current_dir)


os.chdir("C:\\github\\coursera")
import os
def parent_directory():
  # Create a relative path to the parent 
  # of the current working directory 


    # os.path.join(path1, path2...)
    #
    relative_parent = os.path.join(os.getcwd() , os.pardir)
    print(relative_parent)


  # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)

print(parent_directory())


#####################################################################
# Question 4
#
######################################################################
# The file_date function creates a new file in the current working directory, checks the date that the file was modified, 
# and returns just the date portion of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file 
# called "newfile.txt" and check the date that it was modified.

import os
import datetime

def file_date(filename):
  # Create the file in the current directory

  #basic create blank file
  with open(filename, "w") as file:
    file.write("hello")


  timestamp = os.path.getmtime(filename)
  # Convert the timestamp into a readable format, then into a string
  readable_time = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')
  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return ("{}".format(readable_time))

print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd



############################################
# CSV files
# 
# use "csv" module to parse the files
############################################
# csv.read -> Reading files with csv  
# csv.DictReader -> Reading csv files into a dictionary
#
# csv.writer  -> define object
# csv.writerow -> write output
# csv.DictWrite  -> write from a dictionary

import csv

############
# CSV writer() example
#
############
# Example - Define the data to be written to the CSV file from lists
data = [["Name", "Age", "City"],
        ["John Doe", "32", "New York"],
        ["Jane Doe", "35", "London"]]

# Open the file for writing
with open("c:\\temp\\example.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the data to the file
    writer.writerows(data)


###################
# csv reader() example
#
##################
# The reader() function of the CSV module will interpret the file as a CSV.
# Open the file for reading
with open("c:\\temp\\example.csv", "r") as file:
    reader = csv.reader(file)

    # Read and print the data from the file
    for row in reader:
        print(row)


######################
# Read and write into dictionaries
######################

# DictReader() allows us to convert the data in a CSV file into a standard dictionary. 
# DictWriter() allows us to write data from a dictionary into a CSV file.
# The fieldnames parameter of DictWriter() requires a list of keys
# as this will help DictWriter() organize the CSV rows properly

# Here's an example of how to use the csv.DictReader class in Python to read a CSV file into a list of dictionaries:

with open('c:\\temp\\example.csv', 'r') as file:
    reader = csv.DictReader(file)
    data = list(reader)

print(data)

# this returns
# [{'Name': 'John Doe', 'Age': '32', 'City': 'New York'}, {'Name': 'Jane Doe', 'Age': '35', 'City': 'London'}]


######################################
# Practice quiz
#
#
######################################
# We're working with a list of flowers and some information about each one. The create_file function writes this information to a CSV file. 
# The contents_of_file function reads this file into records and returns the information in a nicely formatted block. 
# Fill in the gaps of the contents_of_file function to turn the data in the CSV file into a dictionary using DictReader
print("PRACTICE QUIZ - Question 1!!!!!\n\n")

import os
import csv

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
  #initialise  
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

# Open the file
  with open('c:\\temp\\flowers.csv', 'r') as file:

    # Read the rows of the file into a dictionary
    reader = csv.DictReader(file)

    # The list function is used to convert an iterable object, in this case the reader object, into a list.
    # this creates 5 dictionaries. One line equals a dictionary
    data = list(reader)  

    # data looks like
    # [{'name': 'carnation', 'color': 'pink', 'type': 'annual'}, 
    # {'name': 'daffodil', 'color': 'yellow', 'type': 'perennial'}, 
    # {'name': 'iris', 'color': 'blue', 'type': 'perennial'}, 
    # {'name': 'poinsettia', 'color': 'red', 'type': 'perennial'}, 
    # {'name': 'sunflower', 'color': 'yellow', 'type': 'annual'}]


    # Process each item of the dictionary
    for row in data:
        return_string += "a {} {} is {}\n".format(row["color"], row["name"], row["type"])

    #print(data)
   
    
    return return_string
    
 #Call the function
print(contents_of_file("c:\\temp\\flowers.csv"))


######################################
# Practice quiz
#
#
######################################
# Using the CSV file of flowers again, fill in the gaps of the contents_of_file function to process the data without turning it into a dictionary. 
# How do you skip over the header record with the field names?
print("PRACTICE QUIZ - Question 2!!!!!\n\n")

# Create a file with data in it
def create_file(filename):
  with open(filename, "w") as file:
    file.write("name,color,type\n")
    file.write("carnation,pink,annual\n")
    file.write("daffodil,yellow,perennial\n")
    file.write("iris,blue,perennial\n")
    file.write("poinsettia,red,perennial\n")
    file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
  create_file(filename)

  # Open the file
  with open('c:\\temp\\flowers.csv', 'r') as file:

    # Read the rows of the file into a LIST
    # each row is 1 string in the LIST
    # ['name,color,type\n', 'carnation,pink,annual\n', 'daffodil,yellow,perennial\n', 'iris,blue,perennial\n', 'poinsettia,red,perennial\n', 'sunflower,yellow,annual\n']
    rows = file.readlines()


    # Process each row, but starting at the second line
    # We can skip the header by using line[1:] to bypass the first row
    for row in rows[1:]:
        

      ########
      #  useful to splt and remove newlines
      # ######  
      # eg. 'carnation,pink,annual\n'
      # split the string by ","
      word = row.rstrip().split(",")

     
      # Format the return string for data rows only

      return_string += "a {} {} is {}\n".format(word[1], word[0], word[2])
     

  return return_string

#Call the function
print(contents_of_file("c:\\temp\\flowers.csv"))



9:39pm










