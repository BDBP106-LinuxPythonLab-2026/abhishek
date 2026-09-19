#Write a program to print the factorial of a number
num = int(input("Enter a number: "))
factorial = 1

while num > 0:
    factorial = factorial * num
    num = num - 1

print(f"The factorial of {num} is {factorial}")
