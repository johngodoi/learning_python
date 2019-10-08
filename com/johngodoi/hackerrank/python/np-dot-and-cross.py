import numpy

dimensions = [int(x) for x in input().split(" ")]
array1 = []
for i in range(dimensions[0]):
    array1.append([int(x) for x in input().split(" ")])
array2 = []
for i in range(dimensions[0]):
    array2.append([int(x) for x in input().split(" ")])

narray1 = numpy.array(array1)
narray2 = numpy.array(array2)
print(numpy.dot(narray1, narray2))

