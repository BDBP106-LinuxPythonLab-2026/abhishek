from utils import math_utils,string_utils

# Mathematical operations
a = 39
b = 30

print("Addition:", math_utils.add(a, b))
print("Subtraction:", math_utils.subtract(a, b))
print("Multiplication:", math_utils.multiply(a, b))
print("Division:", math_utils.divide(a, b))
print("Remainder:", math_utils.remainder(a, b))

# String operations
s1 = "265HSBDB"
s2 = "026"

print("Uppercase:", string_utils.to_uppercase(s1))
print("Lowercase:", string_utils.to_lowercase(s1))
print("Concatenation:", string_utils.concatenate(s1, s2))
