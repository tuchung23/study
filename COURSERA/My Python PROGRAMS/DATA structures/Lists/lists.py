#lists are like arrays essentially containing elements. Can be mixed data types
my_list=[1,2,"hangy"]
print(my_list)

#print the third item as the list starts from 0
print(my_list[2])

# add new item to end of list
my_list.append("boo")
print(my_list)

#append anotther list
my_list.append(["jon", "snow"])
print(my_list)

#delete last item from list using pop
my_list.pop()
print(my_list)

#change content of list
my_list[2]="Annie"
print(my_list)


######
# Use TUPLES for lists that never change
######