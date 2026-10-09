# Write a program to concatenate a list of strings to make a sentence using reduce function.
from functools import reduce
w=["Abhishek","is","a","good","Boy"]
S=reduce(lambda x,y:x+" "+y,w)
print(S)