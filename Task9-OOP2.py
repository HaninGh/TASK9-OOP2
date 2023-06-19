class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())


# a rectangle object
rect = Rectangle(10, 5)

# the properties of the rectangle object
rect.display()

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def display(self):
        print("Length:", self.length)
        print("Width:", self.width)
        print("Perimeter:", self.perimeter())
        print("Area:", self.area())


class Parallelepipede(Rectangle):

    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


# a parallelepipede object
parallelepipede = Parallelepipede(10, 5, 3)

# the properties of the parallelepipede object
parallelepipede.display()

# Calculate the volume of the parallelepipede
volume = parallelepipede.volume()

# Print the volume
print("Volume:", volume)