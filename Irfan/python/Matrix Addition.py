# Step 1: Take number of rows and columns as input
row = int(input("Number of rows: "))
column = int(input("Number of columns: "))

matrix_1 = []
matrix_2 = []
result = []

print("\nEnter values for Matrix 1:")
for i in range(row):
    temp = []
    for j in range(column):
        val = int(input(f"Matrix 1[{i}][{j}]: "))
        temp.append(val)
    matrix_1.append(temp)


print("\nEnter values for Matrix 2:")
for i in range(row):
    temp = []
    for j in range(column):
        val = int(input(f"Matrix 2[{i}][{j}]: "))
        temp.append(val)
    matrix_2.append(temp)


for i in range(row):
    temp = []
    for j in range(column):
        temp.append(matrix_1[i][j] + matrix_2[i][j])
    result.append(temp)


print("\nMatrix 1:")
for r in matrix_1:
    print(r)

print("\nMatrix 2:")
for r in matrix_2:
    print(r)

print("\nResult (Matrix 1 + Matrix 2):")
for r in result:
    print(r)
