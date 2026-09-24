B = input("Enter binary number: ")
D = 0

for i in B:
    # Multiply the current total by 2 and add the next digit
    D = D * 2 + int(i)

print("Decimal number:", D)

