# Write a program with a function to calculate the area of a triangle using the formula,
# where a, b, c are sides of the triangle, also providing a test case output from the program
#Area=root s(s − a)(s − b)(s − c) where 2s = a + b + c.
a=12
b=12
c=12
s=(a+b+c)/2
Area= ((s*(s-a)*(s-b)*(s-c))**(1/2))
print(Area)