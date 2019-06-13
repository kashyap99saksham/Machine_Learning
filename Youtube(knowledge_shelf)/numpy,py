import numpy as np   #np is a nick name of numpy , we will use as np : use for mathematical

# HOW TO USE numpy
li = [1,2,3,4,5]
arr = np.array(li)
print(type(arr))    #<class 'numpy.ndarray'>

#NUMPY FUNCTIONS : ALL WORK IS IN FORM OF ARRAY
print(np.arange(1,11))      #[ 1  2  3  4  5  6  7  8  9 10] work as range function and make array not only no.
print(np.arange(1,11,2))    #[1 3 5 7 9]
print(np.zeros(5))      #[0. 0. 0. 0. 0.] GIVES IN FLOATING NO.  | 5 IS COLOUM
print(np.zeros((5,5)))  # [[0. 0. 0. 0. 0.]     GIVE DIMENTIONS IN FORM OF TUPLE
                        #  [0. 0. 0. 0. 0.]
                        #  [0. 0. 0. 0. 0.]
                        #  [0. 0. 0. 0. 0.]
                        #  [0. 0. 0. 0. 0.]]

print(np.ones(5))       #[1. 1. 1. 1. 1.]

print(np.ones((3,5)))   #[[1. 1. 1. 1. 1.]
                        #  [1. 1. 1. 1. 1.]
                        #  [1. 1. 1. 1. 1.]]

print(np.random.randint(0,100))     #GIVE ANY RANDOM VALUE


#IF YOU WANT ARRAY OF RANDOM NUMBERS 
print(np.random.randint(1,100,(3,3)))       #[[71 90 93]        gives 3*3 matrix of rand no.'s 
                                            #  [30 77 91]
                                            #  [43 86  4]] 


arr = np.random.seed(5)     #CONTAIN SAME VALUES ALWAYS
arr = np.random.randint(0,100,10)
print(type(arr))    #<class 'numpy.ndarray'>
print(arr.min())
print(arr.max())
print(arr.mean())   #calculate average value
print(arr.argmax()) #calculate index of max no.
# FOR CHANGE ROW AND COLOUM
print(arr.reshape(2,5))     #[[99 78 61 16 73]  two rows and 5 coloumns
                            #[ 8 62 27 30 80]]
print(np.arange(0,100).reshape(10,10))      #[[ 0  1  2  3  4  5  6  7  8  9]
                                            #  [10 11 12 13 14 15 16 17 18 19]
                                            #  [20 21 22 23 24 25 26 27 28 29]
                                            #  [30 31 32 33 34 35 36 37 38 39]
                                            #  [40 41 42 43 44 45 46 47 48 49]
                                            #  [50 51 52 53 54 55 56 57 58 59]
                                            #  [60 61 62 63 64 65 66 67 68 69]
                                            #  [70 71 72 73 74 75 76 77 78 79]
                                            #  [80 81 82 83 84 85 86 87 88 89]
                                            #  [90 91 92 93 94 95 96 97 98 99]]

mat = np.arange(0,100).reshape(10,10)
print(mat[0,2])     #2
print(mat[0,:])     #first row [ 0 10 20 30 40 50 60 70 80 90]
print(mat[:,0])     #coloumn [ 0 10 20 30 40 50 60 70 80 90]
print(mat[0:3,0:3])     #[[ 0  1  2]
                        #  [10 11 12]
                        #  [20 21 22]]
