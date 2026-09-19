
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual rate of interest in %: "))
time = float(input("Enter the time period in years: "))

simple_interest = (principal * rate * time) / 100

total_amount = principal + simple_interest

print(f"Simple Interest: {simple_interest:.3f}")
print(f"Total Amount: {total_amount:.3f}")
