#Write a program to filter out the odd elements of the Fibonacci series for the first n terms.
n=int(input("Enter a number:",))
a,b=0,1
fib=[]
for i in range(n):
    fib.append(a)
    a,b=b,a+b
odd=list(filter(lambda x: x%2!=0,fib))
print("Fibonacci Series:",fib)
print("Odd elements of Fibonacci Series:",odd)