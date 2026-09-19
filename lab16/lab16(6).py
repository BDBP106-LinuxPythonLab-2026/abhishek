

num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10    # Gets the last digit
    sum += digit        # Adds the digit to the running total
    num //= 10          # Removes the last digit by integer division

print("Sum of digits =", sum)
