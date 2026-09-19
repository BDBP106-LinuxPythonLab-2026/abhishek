#Write a program to check if an input string is palindrome
str = input("Enter a string: ")
original_str = str
reversed_str = ""

for i in str:
    reversed_str = i + reversed_str

if original_str == reversed_str:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
