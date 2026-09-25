#Write a program to find the maximum and minimum values of a dictionary.
D={'grapes':6,'apple':5,'banana':7,'mango':9}
min=D.get('grapes')
max=D.get('grapes')
for value in D.values():
    if value < min:
        min=value
    if value > max:
        max=value
print("minimum value:", min)
print("maximum value:", max)