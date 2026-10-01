#i) Using a simple do loop structure or list comprehension, find the sum of elements in the above list a.
a=[i for i in range(1,51)]
total=0
for i in a:
    total=total+i
print(total)

#ii)Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
b = [i for i in range(2, 51) if all(i % j != 0 for j in range(2, i))]
print(b)

#iii)
c = []
i = 0
while i < len(a):
    if a[i] in b:
        c.append(a[i])
    i = i + 1
print(c)
