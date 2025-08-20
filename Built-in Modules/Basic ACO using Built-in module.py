#Calculating func area using math functions
# This script calculates the area of a circle using the math module in Python.
import math  # Importing the math module
radius = float(input("Enter the radius of the circle: "))  # Taking user input for radius
area = math.pi * (radius ** 2)  # Calculating the area using the formula πr²
print("The area of the circle with radius", radius, "is", area)  # Displaying the calculated area
# Displaying the value of pi
print("The value of pi is", math.pi)  # Displaying the value of pi
#calculating circumference
circumference = 2 * math.pi * radius  # Calculating the circumference using the
# formula 2πr
print("The circumference of the circle with radius", radius, "is", circumference)  # Displaying the calculated circumference
# circumference
# Displaying the value of pi
print("The value of pi is", math.pi)  # Displaying the value of pi
# volume of sphere
volume = (4/3) * math.pi * (radius ** 3)  #
#Calculating the volume of a sphere using the formula (4/3)πr³
print("The volume of the sphere with radius", radius, "is", volume) # Displaying the calculated volume

