import numpy as np

matrix1 = [[1, 2, 3, 4, 5],
          [6, 7, 8, 9, 10],
          [11, 12, 13, 14, 15]]

matrix2 = [[1, 2],
          [3, 4],
          [5, 6],
          [7, 8],
          [9, 10]]

product = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
for i in range(len(matrix1)):  # iterate over rows of matrix1
    for j in range(len(matrix2[0])):  # iterate over columns of matrix2
        for k in range(len(matrix2)):  # iterate over rows of matrix2
            product[i][j] += matrix1[i][k] * matrix2[k][j]

print(product)

# Using numpy
# Create a 3x5 matrix 
np_matrix1 = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
])

# Create a 5x2 matrix 
np_matrix2 = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 10]
])

np_product = np.matmul(np_matrix1, np_matrix2)
print(product)
