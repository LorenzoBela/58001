class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

    def diameter(self):
        return 2 * self.radius

radius = float(input("Enter the radius of the circle in meters: "))
enzo = Circle(radius)
print("A circle with a radius of {} meters, has an area of {:.2f} square meters, and a perimeter of {:.2f} meters.".format(enzo.radius, enzo.area(), enzo.perimeter()))

choice = input("Do you want to know the diameter of the circle? (y/n) ")
if choice.lower() == "y":
    print("The diameter of the circle is {:.2f} meters.".format(enzo.diameter()))

print("Thank you for using the program!")
