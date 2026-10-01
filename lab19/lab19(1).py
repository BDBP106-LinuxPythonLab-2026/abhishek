#Long Format
# a=[]
# for i in range(1, 51):
#     a.append(i)
# print(a)

#List Comprehension
print("i)Create a list spanning 1 to 50 using list comprehension method. Call this list a.")

a=[i for i in range(1,51)]    #The first i tells Python Put the current value of i into the new list(a)
print(a)

print("ii)Slicing with positive step:")
#a
print("(a) output :", a[1:5])
#b
print("(b) output :", a[3:20:2])
#c
print("(c) output :", a[::2])
#d
print("(d) output :", a[::])
#e
print("(e) output :", a[10::2])
#f
print("(f) output :", a[1:1:1])
#g
print("(g) output :", a[:0:])
#h
print("(h) output :", a[-7::1])
#i
print("(i) output :", a[-6:])
#j
print("(j) output :", a[-10:-4])

print("(iii) Slicing with negative step:")
#a
print("(a) output :", a[::-1])  # to reverse the integer or string
#b
print("(b) output :", a[::-3])
#c
print("(c) output :", a[:1:-2])
#d
print("(d) output :", a[-1:-1:-1])
#e
print("e) output :", a[:-5:-1])
#f
print("f) output :", a[:0:-1])
#g
print("g) output :", a[:-1:-1])
#h
print("h) output :", a[0:-5:-1])
#i
print("i) output :", a[-1:5:-1])
#j
print("j) output :", a[2:2:-1])
#k
print("k) output :", a[2:1:-1])
#l
print("l) output :", a[0:-5])

print("iv) Modification of lists using list slicing:")

print("(a) Create a list of even numbers from a using list slicing technique.")
print(a[1::2])

print("(b) Create a new list from a by choosing the first 10 numbers, then the even numbers from 35-50.")
L= a[:10] + a[35:50:2]
print(L)

