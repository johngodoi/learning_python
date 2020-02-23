import numpy as np

dim = [int(i) for i in input().strip().split(' ')]

print(np.zeros(tuple(dim), dtype = np.int))
print(np.ones(tuple(dim), dtype = np.int))

