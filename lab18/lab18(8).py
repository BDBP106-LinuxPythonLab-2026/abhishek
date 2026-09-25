# Write a program to interchange the even and odd components of an input list. The list
# can contain any type of variables. Output the result for the following example:
L = [23, 32, 33, 44, 'BDBH101', 'hello', 'python', 15, 1e-10, True, 'hit']
for i in range(0, len(L) - 1, 2):     #2 skip value means move to the next even index after processing one pair.
    L[i], L[i + 1] = L[i + 1], L[i]

print(L)
