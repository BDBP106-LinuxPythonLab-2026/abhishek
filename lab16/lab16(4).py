
import math
angle = float(input("Enter angle in degrees: "))
radians = math.radians(angle)

#All the 6 trigonometric functions
sin= math.sin(radians)
cos= math.cos(radians)
tan= math.tan(radians)
cosec = 1 / sin
sec = 1 / cos
cot = 1 / tan
print("sin =", sin)
print("cos =", cos)
print("tan =", tan)
print("cosec =", cosec)
print("sec =", sec)
print("cot =", cot)
