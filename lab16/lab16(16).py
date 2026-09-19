#Write a program to find whether a given triangle is equilateral isosceles or scalene. User input is length of sides.

side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

if side1 == side2 and side2 == side3 and side3 == side1:
    print("it a equilatoral triangle")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("it an isosceles triangle")
else:
    print("it is a scalene triangle")