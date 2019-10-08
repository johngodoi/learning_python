import numpy

dimensions = numpy.array(input().split(" "), int)

values = []
for i in range(dimensions[0]):
    values.append([int(x) for x in input().split(" ")])

narray = numpy.array(values)

print(numpy.prod(numpy.sum(narray, axis=0)))

