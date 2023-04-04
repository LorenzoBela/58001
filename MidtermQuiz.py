class DistanceConverter:
    def __init__(self, distance, unit):
        self.__distance = distance
        self.__unit = unit

    def __convert_to_cm(self):
        if self.__unit == "meter":
            return self.__distance * 100
        elif self.__unit == "centimeter":
            return self.__distance
        elif self.__unit == "kilometer":
            return self.__distance * 100000
        elif self.__unit == "inch":
            return self.__distance * 2.54

    def __convert_to_km(self):
        if self.__unit == "meter":
            return self.__distance / 1000
        elif self.__unit == "centimeter":
            return self.__distance / 100000
        elif self.__unit == "kilometer":
            return self.__distance
        elif self.__unit == "inch":
            return self.__distance * 0.0000254

    def __convert_to_in(self):
        if self.__unit == "meter":
            return self.__distance * 39.37
        elif self.__unit == "centimeter":
            return self.__distance * 0.3937
        elif self.__unit == "kilometer":
            return self.__distance * 39370.08
        elif self.__unit == "inch":
            return self.__distance

    def get_conversions(self):
        cm = self.__convert_to_cm()
        km = self.__convert_to_km()
        inches = self.__convert_to_in()
        return "{} {} is equal to {:.2f} centimeters, {:.6f} kilometers, and {:.2f} inches.".format(self.__distance, self.__unit, cm, km, inches)

distance = float(input("Enter the distance: "))
unit = input("Enter the unit (meter/centimeter/kilometer/inch): ")
converter = DistanceConverter(distance, unit)
print(converter.get_conversions())
