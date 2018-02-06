#05_01_converter
class ScaleConverter:
    #The __init__ is called when a class is insantiated.
    #self is required for __init__, though not the call to it
    def __init__(self, units_from, units_to, factor):
        #notice the use of variable shadowing here
        self.units_from = units_from
        self.units_to = units_to
        self.factor = factor

    #note that all of the methods have self as a parameter
    def description(self):
        return 'Convert ' + self.units_from + ' to ' + self.units_to

    #multiplies the factor of the object by a value passed in
    def convert(self, value):
        return value * self.factor

#05_03_converter_inheritance
class ScaleAndOffsetConverter(ScaleConverter):

    def __init__(self, units_from, units_to, factor, offset):
        ScaleConverter.__init__(self, units_from, units_to, factor)
        self.offset = offset

    def convert(self, value):
        return value * self.factor + self.offset

