# Write a program to find the sum of all the elements in a list using lambda and reduce functions
from functools import reduce
E=[23,2,34,45]
sum=reduce(lambda x,y:x+y,E)
print(sum)