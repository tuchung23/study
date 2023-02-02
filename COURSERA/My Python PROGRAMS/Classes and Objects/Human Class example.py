
class Human:
    # every human should have a name and gender
    # initialise the object
    # these defaults exist in all methods
    def __init__(self, name , gender):
        self.name=name
        self.gender=gender


     # first method function
     # the object just calls this method with no arguments
    def speak_name(self):
        print("My name is %s" % self.name)


    def speak(selfself,text):
        print(text)


    def perform_math_task(self, math_operation, *args):
            print ("%s performed a math operation and the result was: %f" % (self.name, math_operation(*args)) )


# outside function
def add(a,b):
        return (a+b)


# define my object=Tu=self
Tu=Human("Tu Chung" , "Male")


Tu.speak("hi mate")

# passing a function as a parameter
Tu.perform_math_task(add, 5, 10)