import numpy as np

dim = [int(i) for i in input().strip().split(' ')]
np.set_printoptions(sign=' ')
print(np.eye(dim[0], dim[1]))