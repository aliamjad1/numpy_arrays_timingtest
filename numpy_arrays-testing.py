# import numpy
# arr=numpy.array ([[[1,2,3,4],[5,6,7,8]], [[9,10,11,12],[13,14,15,16]]])
# print(arr[0:2,0])

# x=(5)
# print(x)
# arr=numpy.array(x)
# print(arr)
# print(type(arr))
import numpy as np
import sys
import time

# size of list
# normal_list = [1, 2, 3]
# print("Size of list each element: ", sys.getsizeof(normal_list))
# print("Size of list: ", sys.getsizeof(normal_list) * len(normal_list))

# using Range function

# normal_list = range(1000)
# # print(normal_list)
# print("Size of list each element: ", sys.getsizeof(normal_list))
# print("Size of list: ", sys.getsizeof(normal_list) * len(normal_list))

# size of Array

# array = np.array([1, 2, 3])
# print("Size of each element array in bytes: ", array.itemsize)
# print("Size of list: ", array.itemsize * len(array))

# using arange function
#
# array = np.arange(1000)
# print("Size of each element array in bytes: ", array.itemsize)
# print("Size of list: ", array.itemsize * len(array))

# find time in list

initial_time = time.time()
size = 1000000
#
# # list
#
list_1 = range(size)
list_2 = range(size)
resultant_list = [(a * b) for a, b in zip(list_1, list_2)]
ending_time = (time.time() - initial_time)
print("List ending time:" + str(ending_time))
#
# # array

initial_time_array = time.time()
array_1 = np.arange(size)
array_2 = np.arange(size)
a = array_1 * array_2
ending_time_array = time.time()
print(ending_time_array - initial_time_array)

list=np.array([[[[1, 2, 3],[4,5,6]],[[7,8,9],[11,12,13]]]])
print(list[0:])
listsize=[1,2,3]
print("\nsize of list= " + str(sys.getsizeof(listsize)))
print("Size of all list elements = " + str(sys.getsizeof(listsize) * len(listsize)) )
arraysize=np.array([1,2,3])
print("size of numpy array= "  + str(arraysize.itemsize))
print("Size of each array element: = " + str(arraysize.itemsize * len(arraysize)))