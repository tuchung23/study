# code inside function MUST be indented
def my_function():
    print("Tu is great")

# input parameter is local to the function
def my_function_2(name):
    print(name + " is great")

#return data
def my_function_3(num1, num2):
    Result=int(num1) + int(num2)
    return Result

my_function()
my_function_2("Tony")

N1= input("Enter a number: ")
N2=input("Enter another number: ")
#Ensure data types concatenated are the same
print("The result is " + str(my_function_3(N1,N2)) )