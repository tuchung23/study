
#open up a file in the same folder as program
# r for read, w for write, r+ for read and write modes
#path="C:\\Users\\s66918\\Desktop\\My PYTHON PROGRAMS\\Read and Write Files\\Employees.txt"


# useful to get the file location
#import os
#print(os.getcwd())

employee_file=open( "C:\\Users\\s66918\\Desktop\\My PYTHON PROGRAMS\\Read and Write Files\\Employees.txt" , "r")

# is file readable? true or false
print(employee_file.readable())


# read the first line ; good for loop iterations as jumps to next line
#print(employee_file.readline())

#read the whole file in existing format
#print(employee_file.read())

# read all the lines and PUT INSIDE a LIST
# this prints the second line as index from 0. Good for traversins a list
#print(employee_file.readlines()[1])

employee_file.close()



######## Now append to file - at the end

employee_file=open( "C:\\Users\\s66918\\Desktop\\My PYTHON PROGRAMS\\Read and Write Files\\Employees.txt" , "a")

#append on new line
employee_file.write("\nTrammi - IT")

employee_file.close()

######## Write to the file will overwrite EVERYTHING!!!! so be careful