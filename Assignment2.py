#Assignment 2 
#Program to calculate the area of a circle 

import math

# Input diameter
diameter = float(input("Enter the diameter of the circle: "))

# Calculate radius
radius = diameter / 2

# Calculate area
area = math.pi * (radius ** 2)

# Print the result
print(f"The area of the circle is: {area:.2f}")
