# Reading the file
with open("stringmatrix.dat", "r") as file:
    lines = file.readlines()

# Creating 2D list
grid = []
for line in lines:
    grid.append(line.split())

print("2D List:", grid)

# Finding rows and columns
rows = len(grid)
cols = len(grid[0])
# Printing columns
columns = []
for j in range(cols):
    column = []
    for i in range(rows):
        column.append(grid[i][j])
    columns.append(column)
print("Columns:", columns)
# Printing diagonals
diagonals = []
for k in range(rows + cols - 1):
    diagonal = []
    for i in range(rows):
        j = k - i
        if 0 <= j < cols:
            diagonal.append(grid[i][j])
    diagonals.append(diagonal)

print("Diagonals:", diagonals)
