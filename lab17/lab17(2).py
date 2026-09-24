#Write a script that computes power - raise base to the n-th power. Eg. power(2, 5).Here base is 2 and n-th power is 5.
base = int(input("Enter base: "))
n = int(input("Enter power: "))
result = 1
for i in range(n):
    result = result * base
print("Result =", result)
