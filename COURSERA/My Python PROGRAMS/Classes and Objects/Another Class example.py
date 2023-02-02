


# a METHOS is a function in a class

class Fridge:
    "This class implements a fridge where ingredients can be added"

    # When python creates object, the _init_ method is what passes the object its first parameter
    # the (self) portion is actually a variable used to represent the instance of the object
    def __init__(self, items={}):
        "optionally pass in an initial dictionary of itemsv "

        # check if its dictionary
        if type(items) != type({}):
            raise TypeError("Fridge requires a dictionary but was given %s" % type(items))

        self.items=items
        return

    #def add_one(self, food_name):
     #   n n



var1=Fridge({"cheese":3, "potato":3})
print(var1)