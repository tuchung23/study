##########################################
# PYTHON via Coursera
#
# Print, Boolean , Ranges , If and While statements
#
##########################################

print("#######################")
print("PRINTING BASICS")
print("#######################")

print("Hello World")

Name="Tu Chung"
print("Hello " + Name)

print(4+6)

# To find out what data type
# this will tell us "A" is a string and 2 is an int, 2.5 is a float
print(type("A"))
print(type(2))
print(type(2.5))

# variables can NOT start with a number or contain a special character like & 
# They must start with a letter or _
# variables are case sensitive

# implicit conversion - interpreter converts one data type into another like below
# Implicit conversion is where the interpreter helps us out and automatically converts one data type into another, without having to explicitly tell it to do so.
print(7+8.5)

print("a" + "b" + "c")

# conversions - like below to convert integer to a string
# explicit conversion is where we manually convert from one data type to another by calling the relevant function for the data type we want to convert to

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is:" + str(average))

print("#######################")
print("DEFINING FUNCTIONS")
print("#######################")


# define functions
# indentation important
# def greeting(name):
#   print("Welcome, " + name)

# function to return a value
def area_triangle(base,height):
   return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(6,5)
sum= area_a + area_b
print("The sum of both areas is: " + str(sum))

# NONE is a special data type in python used to indicate that things are empty or that they returned nothing

###################
###################


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	return miles * 1.6  # approximately 1.6 km in 1 mile

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2 * my_trip_km) )


print("#######################")
print("BOOLEAN BASICS")
print("#######################")

#  Booleans
print("cat" == "dog")   
# returns false
print ( 1 != 2)  
# returns true
# print(1 < "1")  
# returns error type as integer vs string


print("#######################")
print("IF Statements")
print("#######################")

# 
# Branching with IF statements
#  def hint_username(username):
#       if len(username) < 3:
#           print("Invalid username. Must be at least 3 characters long")
#       elif len(username) > 15:
#           print("Invalid username. Must be at most 15 characters long")
#       else:
#           print("Valid username")
#
#
# LOOPS!!!!!!!
#
x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x=x+1
print("x" + str(x))



# FOR loop iterates over a KNOWNsequence of values
# range starts at 0
for x in range(5):
    print(x)

# a list of strings
friends = ['Tu' , 'Mei']
for friend in friends:
    print("hi " + friend)


print("#######################")
print("RANGE BASICS")
print("#######################")

# RANGE function
# range(1,10)   ; from 1 to 20
# range(0,101,10) ; from 0 to 101 in steps of 10


# Break & Continue
# You can interrupt both while and for loops using the break keyword. We normally do this to interrupt a cycle due to a separate condition.

# You can use the continue keyword to skip the current iteration and continue with the next one. This is typically used to jump ahead when some of 
# the elements of the sequence aren’t relevant.

def votes(params):
	for vote in params:
	    print("Possible option:" + vote)


votes(['yes', 'no', 'maybe'])


# Complete the function digits(n) that returns how many digits the number has. For example: 25 has 2 digits and 144 has 3 digits. 
# Tip: you can figure out the digits of a number by dividing it by 10 once per digit until there are no digits left.

def digits(n):
	count = 0
	if n == 0:
	  return 1
	while ( n >= 1 ):
		count += 1
		n = n /10
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1




def counter(start, stop):
	x = start
	if x > stop:
		return_string = "Counting down: "


		while x >= stop:
			return_string += str(x)
			# "Counting down: 2" ; x=2

			if x > stop :
				return_string += ","
				# "Counting down: 2," ; x=2

			x = x - 1
	

	else:
		return_string = "Counting up: "
		while x <= stop:
			return_string += str(x)
			if x < stop:
				return_string += ","
			x = x + 1
	return return_string

print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should be "Counting down: 2,1"
print(counter(5, 5)) # Should be "Counting up: 5"





def even_numbers(maximum):
	return_string = ""
	for x in range(2,maximum+1,2):
		return_string += str(x) + " "
	return return_string.strip()

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed



