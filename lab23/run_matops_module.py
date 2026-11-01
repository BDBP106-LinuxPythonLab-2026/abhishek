import matops
a = [1, 2, 3]
b = [4, 5, 6]

print(matops.dot_product(a, b))


A = [[1, 2],
     [3, 4]]
v = [5, 6]

print(matops.matrix_vector(A, v))

B = [[5, 6],
     [7, 8]]
print(matops.matrix_matrix(A, B))


x = [1, 2, 3]
y = [4, 5, 6]
print(matops.cross_product(x,y))