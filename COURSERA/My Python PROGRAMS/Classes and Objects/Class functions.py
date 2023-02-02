class Student:
    def __init__(self,name,major,gpa,is_on_probation):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation

    # class function to see if a student has honors which is gpa > 3.5. This is a function within the Class itself
    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

# build my student with their attributse
my_student1=Student("Tu", "engineer" , 5.5 , False)


# call a function within the class
print(my_student1.on_honor_roll())