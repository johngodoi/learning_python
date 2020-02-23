import numpy as np

dim = [int(i) for i in input().strip().split(' ')]
matrix1 = []
for i in range(dim[0]):
    matrix1.append(input().strip().split(' '))

matrix2 = []
for i in range(dim[1]):
    matrix2.append(input().strip().split(' '))

np_m1 = np.array(matrix1, int)
np_m2 = np.array(matrix2, int)

print(np.concatenate((np_m1, np_m2), axis=0))


