import numpy

dimensions = [int(x) for x in input().split(" ")]
array = []
for i in range(dimensions[0]):
    array.append([int(x) for x in input().split(" ")])
numpy.set_printoptions(legacy='1.13')
narray = numpy.array(array)
print(numpy.mean(narray, axis=1))
print(numpy.var(narray, axis=0))
print(numpy.std(narray))
