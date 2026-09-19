# Write a code to get the Fibonacci numbers beginning with f0 = 0 and f1 = 1 up to f25.
# Note: You’ll have to think about how to swap numbers. In case you are not familiar,
# Fibonacci numbers are those belonging to the Fibonacci series where each number is the
# sum of the previous two numbers. For example, 1,2,3,5,8,. . . . In this question, the
# Fibonacci series will start from the numbers 0,1.

f0 = 0
f1 = 1

print(f0)
print(f1)

for i in range(2, 26):
    f2 = f0 + f1
    print(f2)

    f0 = f1
    f1 = f2
