# can use to define a new type alongside strings, numbers and boolean

#use a class to define what the object is

class Student:

    # init pretty much means to initialise the characteristics of the class
    # SELF refers to the object
    def __init__(self,name,major,gpa,is_on_probation):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation



# create a my_student1 object. So basically SELF=MY_STUDENT1
my_student1=Student("Tu", "engineer" , 5.5 , False)


# print the name of my first student object
print(my_student1.name)