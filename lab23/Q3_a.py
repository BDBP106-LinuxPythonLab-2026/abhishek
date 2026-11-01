with open("stringmatrix.dat", "w") as file:

    for i in range(65, 77, 4):
        file.write(chr(i) + " " + chr(i+1) + " " + chr(i+2) + " " + chr(i+3) + "\n")

print("File created successfully!")
