##Numpy :
##    pip install numpy
##    it stands for numerical and fundamental python packages
##    for specific computing tools and technique to solve mathematical problems

##1- one dimensional array
##2- two dimensional array
##3- three dimensional array

##Syntax :
##import numpy
##var=numpy.array("values")    

##1. One dimensional array :

##import numpy
##a=numpy.array([1,2,3,4,5,9])
##
##print(a.ndim)
##print(a.shape)

##2. Two dimensional array :

##import numpy
##a=numpy.array([[1,2,4,6],[3,4,6,8],[6,7,8,9]])
##
##print(a.ndim)
##print(a.shape)

##3. Three dimensional array :

##import numpy
##a=numpy.array([[[1,2,4,6],[3,4,6,8],[6,7,8,9]]])
##
##print(a.ndim)
##print(a.shape)

##slicing :

##import numpy as n
##a=n.array([1,2,3,4])
##print(a[2])
##
##a[2]=10
##c=a[1:]
##print(a)
##print(c)

##import numpy as np
##a=np.array([(2,3,6),(4,5,8),(1,2,3)])
####print(a[1:,1:])
##print(a[1:2,1:2])


#giving the dimension value as a range order

##import numpy as np
##a=np.arange(10)
##print(a)

#Ones(),zeros()

##import numpy as np
##a=np.zeros([5,3])
##print(a)
##b=np.ones([3,5])
##print(b)

#reshapes()

##import numpy as np
##a=np.reshape([1,2,3,4,5,6,7,8,10,20],(2,5))
##print(a)

##import numpy as np
##a=np.arange(1,10,2)
##print(a)

#arithmetic operations in numpy :
##import numpy as np
##a=np.array([1,2,3,4,5])
##b=np.array([6,7,8,9,10])
##c=np.add(a,b)
##print(c)

#where()

##import numpy as np
##a=np.array([1,2,3,4,5])
##b=np.where(a==3)
##print(b)
##c=np.max(a)
##print(c)
##d=np.min(a)
##print(d)



































