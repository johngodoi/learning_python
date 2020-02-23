import numpy as np

dim = [int(i) for i in input().strip().split(" ")]
matrix = []
for i in range(dim[0]):
    row = input().strip().split(' ')
    matrix.append(row)

np_matrix = np.array(matrix, int)
print(np.transpose(np_matrix))
print(np_matrix.flatten())