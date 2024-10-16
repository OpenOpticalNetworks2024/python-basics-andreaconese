"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt
from numpy.ma.extras import average


# ex1
def exercise1():
    # Accepting two integer inputs from the user
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Calculating the product
    product = num1 * num2

    # If the product is greater than 1000, return their sum
    if product > 1000:
        return num1 + num2
    else:
        return product


# ex2
def exercise2(start, end):
    # Initialize the previous number as 0 for the first iteration
    previous_number = 0

    # Iterate through the range from start to end
    for i in range(start, end + 1):
        # Calculate the sum of the current and previous numbers
        current_sum = i + previous_number

        # Print the result
        print(f"Current Number: {i}, Previous Number: {previous_number}, Sum: {current_sum}")

        # Update the previous number for the next iteration
        previous_number = i

    # Example usage: range from 1 to 5



# ex3
def exercise3():
    # give a list of ints
    list1 = [10, 20, 30, 40, 50]
    # return True if first and last number of a list is same
    if list1[0] == list1[-1]:
        print('True')
    else:
        print('False')


# ex4
def exercise4():
    # Given a list of numbers, Iterate it and print only those numbers which are
# divisible of 5
    list1 = [10, 20, 33, 46, 55]
    for num in list1:
        if num % 5 == 0:
            print(num)


# ex5
def exercise5():
    # Return the number of times that the string “Emma” appears anywhere in
# the given string: “Emma is a good developer. Emma is also a writer”
    string = "Emma is a good developer. Emma is also a writer"
    print(string.count("Emma"))


# ex6
def exercise6():
    # Given a two list of ints create a third list such that should contain only
# odd numbers from the first list and even numbers from the second list
    list1 = [10, 20, 23, 11, 17]
    list2 = [13, 43, 24, 36, 12]
    list3 = []
    for num in list1:
        if num % 2 != 0:
            list3.append(num)
    for num in list2:
        if num % 2 == 0:
            list3.append(num)
    print(list3)


# ex7
def exercise7():
    # Given 2 strings, s1 and s2, create a new string by appending s2 in the
# middle of s1
    s1 = "Ciao Andrea"
    s2 = "sono "
    middle_index = int(len(s1) / 2)
    new_string = s1[:middle_index] + s2 + s1[middle_index:]
    print(new_string)


# ex8
def exercise8():
    # Given 2 strings, s1, and s2 return a new string made of the first, middle
# and last char each input string
    s1 = "Ciao Andrea"
    s2 = "sono"
    new_string = s1[0] + s2[0] + s1[int(len(s1) / 2)] + s2[int(len(s2) / 2)] + s1[-1] + s2[-1]
    print(new_string)


# ex9
def exercise9():
    # Given a string input Count all lower case, upper case, digits, and special
# symbols
    string = "Ciao Andrea 17 %"
    upper_case = 0
    lower_case = 0
    digits = 0
    special_symbols = 0
    for char in string:
        if char.isupper():
            upper_case += 1
        elif char.islower():
            lower_case += 1
        elif char.isdigit():
            digits += 1
        else:
            special_symbols += 1
    print(f"Upper case: {upper_case}, Lower case: {lower_case}, Digits: {digits}, Special symbols: {special_symbols}")


# ex10
def exercise10():
    # Find all occurrences of “USA” in given string ignoring the case
    string = "Welcome to USA. usa, usa, usa"
    print(string.count("usa"))


# ex11
def exercise11():
    string = "Andrea ha 22 anni perchè è nato nel 2002"
    count_digits = 0
    sum_digits = 0

    for char in string:
        if char.isdigit():
            count_digits += 1
            sum_digits += int(char)

    average = sum_digits / count_digits
    print(f"Average: {average}")
    print(f"Sum: {sum_digits}")



# ex12
def exercise12():
    # Given an input string, count occurrences of all characters within a string
    string = "Ciao Andrea"
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    print(char_count)



if __name__ == "__main__":
    print("EXERCISE SET 1")
    print("EX1")
    exercise1()
    print("EX2")
    exercise2(1,2)
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
    print("EX11")
    exercise11()
    print("EX12")
    exercise12()
