#(7) Write a script to check if a number is palindrome or not.
num = int(input("Enter a number: "))
original_num = num
reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10

if original_num == reversed_num:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")

