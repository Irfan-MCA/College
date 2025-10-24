
row = int(input("Enter number of rows: "))
column = int(input("Enter number of columns: "))

matrix = []
print("\nEnter matrix values:")
for i in range(row):
    temp = []
    for j in range(column):
        val = int(input(f"Matrix[{i}][{j}]: "))
        temp.append(val)
    matrix.append(temp)


transpose = []
for j in range(column):
    temp = []
    for i in range(row):
        temp.append(matrix[i][j])
    transpose.append(temp)


print("\nOriginal Matrix:")
for r in matrix:
    print(r)


print("\nTransposed Matrix:")
for r in transpose:
    print(r)
