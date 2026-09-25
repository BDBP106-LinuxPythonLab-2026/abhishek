# Write a function called nextPrime that finds and returns the first prime number larger
# than some integer, n. The value of n will be passed to the function as its only parameter.
# The main program should read an integer from the user and display the first prime
# number larger than the entered value?
n = int(input("Enter number: "))
def nextPrime(n):
    n = n + 1          # Start with next number of given integer(n)

    while True:        # Keep checking until a prime number is found
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            return n

        n = n + 1

print(f"First prime number larger than {n} is", nextPrime(n))

