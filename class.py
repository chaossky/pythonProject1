import numpy 

A = numpy.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13 ,14 ,15, 16]])
print(A)
slice_Y_equal_size = numpy.split(A, 2, axis = 0)
print(slice_Y_equal_size[0])
print(slice_Y_equal_size[1])