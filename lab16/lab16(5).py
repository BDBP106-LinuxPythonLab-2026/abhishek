# (5)Write a program to find the roots of a quadratic equation. Figure out what the inputs
# should be and also have provision to deal with cases where you end up getting complex
# roots.

import math
a=float(input("Enter (a) value: "))
b=float(input("Enter (b) value: "))
c=float(input("Enter (c) value: "))

D=b**2-4*a*c
if a==0:
    print("The equation is undefined")
elif D>0:
    root1=(-b+math.sqrt(D))/(2*a)
    root2=(-b-math.sqrt(D))/(2*a)
    print("Root1=",root1)
    print("Root2=",root2)

elif D == 0:
    root = -b / (2*a)
    print("Both roots are equal:", root)
else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-D) / (2 * a)
    print("Root1 =", real, "+", imaginary,"i")
    print("Root2 =", real, "-", imaginary,"i")