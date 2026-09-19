#Write a program to tell which quadrant a given point lies in the first, second, third or fourth quadrant
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("The point lies in the First Quadrant")
elif x < 0 and y > 0:
    print("The point lies in the Second Quadrant")
elif x < 0 and y < 0:
    print("The point lies in the Third Quadrant")
elif x > 0 and y < 0:
    print("The point lies in the Fourth Quadrant")
else:
    print("The point lies on an axis")
