#Write a program to sum all the values of a dictionary.
D={'grapes':6,'apple':5}
sum= 0
for key in D:
    sum += D.get(key)   # it gets a value of key and get sum

print("Sum =", sum)
