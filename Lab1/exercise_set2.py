"""Exercise Set 2: Data Structures"""

import numpy as np
import matplotlib as plt


# Please, remove all the pass in the exercises and substitute them with the expected methods for your functions


# ex1
def exercise1():
    listOne = [3, 6, 9, 12, 15, 18, 21]
    listTwo = [4, 8, 12, 16, 20, 24, 28]
    listThree = listOne[1::2] + listTwo[::2]
    print(listThree)



# ex2
def exercise2():
    # Given an input list removes the element at index 4 and add it to the 2nd
# position and also, at the end of the list
    sampleList = [34, 54, 67, 89, 11, 43, 94]
    element = sampleList.pop(4)
    sampleList.insert(2, element)
    print(sampleList)

# ex3
def exercise3():
    # Given a list slice it into a 3 equal chunks and revert each list
    sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
    chunkSize = 3
    for i in range(0, len(sampleList), chunkSize):
        print(sampleList[i:i + chunkSize][::-1])


# ex4
def exercise4():
    # Given a list iterate it and count the occurrence of each element and create
# a dictionary to show the count of each element
    sampleList = [11, 45, 8, 11, 23, 45, 23, 45, 89]
    countDict = dict()
    for element in sampleList:
        if element in countDict:
            countDict[element] += 1
        else:
            countDict[element] = 1
    print(countDict)


# ex5
def exercise5():
    # Given a two list of equal size create a set such that it shows the element
# from both lists in the pair
    firstList = [2, 3, 4, 5, 6, 7, 8]
    secondList = [4, 9, 16, 25, 36, 49, 64]
    result = zip(firstList, secondList)
    resultSet = set(result)
    print(resultSet)


# ex6
def exercise6():
    # Given a following two sets find the intersection and remove those elements
# from the first set
    firstSet = {23, 42, 65, 57, 78, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}
    intersection = firstSet.intersection(secondSet)
    for item in intersection:
        firstSet.remove(item)
    print(firstSet)



# ex7
def exercise7():
    # Given two sets, Checks if One Set is Subset or superset of Another Set. if
# the subset is found delete all elements from that set
    firstSet = {57, 83, 29}
    secondSet = {57, 83, 29, 67, 73, 43, 48}
    print(firstSet.issubset(secondSet))
    print(secondSet.issuperset(firstSet))
    if firstSet.issubset(secondSet):
        firstSet.clear()
    if secondSet.issuperset(firstSet):
        secondSet.clear()
    print(firstSet)
    print(secondSet)



# ex8
def exercise8():
    # Iterate a given list and Check if a given element already exists in a dictio-
# nary as a key’s value if not delete it from the list
    original_list = [47, 64, 69, 37, 76, 83, 95, 97]
    sampleDict = {'hon': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

    filtered_list = []
    for item in original_list:
        # Controllare se l'elemento esiste nei valori del dizionario
        if item in sampleDict.values():
            # Se esiste, aggiungere l'elemento alla lista filtrata
            filtered_list.append(item)

    original_list = filtered_list

    # Stampa la lista filtrata
    print(original_list)


# ex9
def exercise9():
    # Given a dictionary get all values from the dictionary and add it in a list
# but don’t add duplicates
    speed = { ' Jan ' :47 , ' Feb ' :52 , ' March ' :47 , ' April ' :44 , ' May ' :52 ,   ' June ' :53 ,  ' July ' :54 , 'Aug' :44 , ' Sept ' :54}
    speedList = []
    for item in speed.values():
        if item not in speedList:
            speedList.append(item)
    print(speedList)


# ex10
def exercise10():
    # Remove duplicate from a list and create a tuple and find the minimum
# and maximum number
    sampleList = [87, 52, 44, 53, 54, 87, 52, 53]
    unique_list = []


    for item in sampleList:
        if item not in unique_list:
            unique_list.append(item)

    unique_tuple = tuple(unique_list)

    minimum_value = min(unique_tuple)
    maximum_value = max(unique_tuple)
    print(maximum_value)
    print(minimum_value)



if __name__ == "__main__":
    print("EXERCISE SET 2: Data Structures")
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
    print("EX9")
    exercise9()
    print("EX10")
    exercise10()
