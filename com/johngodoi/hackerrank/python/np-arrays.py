import numpy


def arrays(array):
    # complete this function
    # use numpy.array
    return numpy.array(array[::-1], float)


arr = input().strip().split(' ')
result = arrays(arr)
print(result)