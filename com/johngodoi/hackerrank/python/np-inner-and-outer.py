import numpy

a1 = numpy.array([int(x) for x in input().split(" ")])
a2 = numpy.array([int(x) for x in input().split(" ")])

print(numpy.inner(a1,a2))
print(numpy.outer(a1,a2))


