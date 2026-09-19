#Write a program to find the distance between 2 points, input is coordinates for the two points.


import math

x1 = float(input("Enter x-coordinate of first point (x1): "))
y1 = float(input("Enter y-coordinate of first point (y1): "))
x2 = float(input("Enter x-coordinate of second point (x2): "))
y2 = float(input("Enter y-coordinate of second point (y2): "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")