#Write a script to check if a given number, N, is prime or not
n = int(input("Enter number: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")


