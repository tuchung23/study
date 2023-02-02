# try except is to catch errors that may otherwise stop your program when you dont want it to

try:
    number= int(input("Enter a number: "))
    print(number)

except:
    # for scenarios where the input is a string instead of a number
    print("invalid input")