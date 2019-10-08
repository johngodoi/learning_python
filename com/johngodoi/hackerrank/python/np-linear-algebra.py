import numpy

dimension = int(input())
values = []
for i in range(dimension):
    values.append([float(x) for x in input().split(" ")])

print(round(numpy.linalg.det(values), 2))

