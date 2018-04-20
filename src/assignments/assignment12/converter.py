#In file converter.py class create a class named Converter with no constructor
# and one method named get_miles_from_km with a km parameter that returns
# the miles given kilometers.


class Converter():

    def get_miles_from_km(self, km):
        return "{0:.2f}".format(km*.621371)
