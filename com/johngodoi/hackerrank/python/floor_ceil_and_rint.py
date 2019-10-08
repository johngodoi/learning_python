import numpy

array = numpy.array([float(x) for x in input().split(" ")])
numpy.set_printoptions(sign=' ')
print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))