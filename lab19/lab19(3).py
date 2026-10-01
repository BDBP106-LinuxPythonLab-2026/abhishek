#i)
#a
a=[i for i in range(1,51)]
x=",".join([str(i) for i in a])
print(x)

#b
a=[i for i in range(1,51)]
x=".".join([str(i) for i in a])
print(x)

#c
a=[i for i in range(1,51)]
x="_".join([str(i) for i in a])
print(x)
#d
a=[i for i in range(1,51)]
x=[ str(i)+ " " + str(i*i) for i in a]
print("\n".join(x))

#ii)
#a
p = ["abhishek tiwari","dhruv shukla","shravan kamble","akash yadav"]
P= [ i.upper() for i in p]
print(P)

#b
P2=[' '.join([i.split()[1],i.split()[0]])for i in p]
print(P2)

#c
P = [i.title().replace(' ', '.') for i in p]
print(P)

#iii)
s= "She sells sea shells that she collects from the sea floor"
w= s.split()
longests = [i for i in w if len(i) == max([len(j) for j in w])]
print(longests)

#iv)
s= "She sells sea shells that she collects from the sea floor"
w= s.lower().split()
duplicate = [i for i in w if w.count(i) > 1]
print(set(duplicate))

