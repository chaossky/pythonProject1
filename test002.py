import numpy

A = numpy.array([[1,4,5,8], [2,1,7,3], [5,4,5,9]])
B=A.reshape(6,2)
print(B)
print("--------------------")
B=numpy.concatenate((B,[[2,2],[5,3]]),axis=0 )
print(B)
    

    # 3

    # 4

    # 5
   