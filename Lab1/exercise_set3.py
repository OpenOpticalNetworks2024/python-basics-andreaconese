"""Exercise Set 3: Numpy Exercises"""

import numpy as np
import matplotlib as plt

# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    # Create a 4X2 integer array and print its attributes
    arr = np.empty((4, 2), dtype=int)
    print(arr)


# ex2
def exercise2():
    # Create a 5X2 integer array from a range between 100 to 200 such that the
# difference between each element is 10
    arr = np.arange(100, 200, 10).reshape(5, 2)
    print(arr)


# ex3
def exercise3():
    # Given the following numPy array, return the array of items in the third
# column of each row
# [[11 ,22, 33], [44, 55, 66], [77, 88, 99]]
    arr = np.array([[11, 22, 33], [44, 55, 66], [77, 88, 99]])
    print(arr[:, 2])



# ex4
def exercise4():
    # Given the following numPy array, return the array of the odd rows and
# the even columns
    arr = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
    print(arr)
    print(arr[::2, 1::2])




# ex5
def exercise5():
    #Add the following two numPy arrays and modify the result array by calulating the square root of each element
    arr1 = np.array([[5, 6, 9], [21 ,18, 27]])
    arr2 = np.array([[15 ,33, 24], [4 ,7, 1]])
    result = arr1 + arr2
    print(result)
    print(np.sqrt(result))



# ex6
def exercise6():
    # Sort following NumPy array:
    arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
    print(np.sort(arr))


# ex7
def exercise7():
    # Given the following numPy array, print the max of axis 0 and the min of
# axis 1
    arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
    print(np.max(arr, axis=0))
    print(np.min(arr, axis=1))


# ex8
def exercise8():
    # Given the following numPy array, delete the second column and insert the
# following new column in its place.
    arr = np.array([[34,43,73],[82,22,12],[53,94,66]])
    new_column = [10,10,10]
    arr = np.delete(arr, 1, axis=1)
    arr = np.insert(arr, 1, new_column, axis=1)
    print(arr)



# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


if __name__ == "__main__":
    print("EXERCISE SET 3: NumPy Exercises")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2()
    print("EX3")
    exercise3()
    print("EX4")
    exercise4()
    print("EX5")
    exercise5()
    print("EX6")
    exercise6()
    print("EX7")
    exercise7()
    print("EX8")
    exercise8()
