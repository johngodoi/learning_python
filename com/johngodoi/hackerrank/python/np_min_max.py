import numpy

dimensions = [int(x) for x in input().split(" ")]
values = []
for i in range(dimensions[0]):
    values.append([int(x) for x in input().split(" ")])

narray = numpy.array(values)
print(numpy.max(numpy.min(narray, axis=1)))
