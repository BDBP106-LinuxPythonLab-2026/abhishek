# Write the above program using lambda expression.
celsius=[10,20,30,40]
fahrenheit=list(map(lambda c:(c*9/5)+32,celsius))
print(fahrenheit)