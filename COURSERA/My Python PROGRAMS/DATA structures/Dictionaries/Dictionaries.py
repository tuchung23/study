#dictionaries are similar to lists but the key differece is they are referenced by names as opposed to their numeric order using a key:value

# created using curly braces
my_dictionary={}
my_dictionary["moses mbye"]=1
my_dictionary["kieran foran"]=7
print(my_dictionary)

# grab just the keys
print(my_dictionary.keys())

#grab the values
print(my_dictionary.values())


monthConversions={
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
}

# print out january corresponding value
print(monthConversions["Jan"])