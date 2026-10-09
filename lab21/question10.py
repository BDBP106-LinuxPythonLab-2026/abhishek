#Write a program to extract all vowels in a given string using list comprehension.
s=input("Enter a string:",)
V=[i for i in s if i.lower() in "aeiou"]
print(V)