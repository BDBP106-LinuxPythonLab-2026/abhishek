#Write a script to check if two strings are anagrams of each other . Eg. listen and silent are anagrams, gram and arm are not anagrams
str1=input("Enter a string1: ")
str2=input("Enter a string2: ")
if sorted(str1) == sorted(str2):
    print("It is Anagrams")
else:
    print("It is not Anagrams")

