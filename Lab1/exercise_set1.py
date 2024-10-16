"""Exercise Set 1: Python Basics"""

import numpy as np
import matplotlib as plt


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
    pass


# ex6
def exercise6():
    pass


# ex7
def exercise7():
    pass


# ex8
def exercise8():
    pass


# ex9
def exercise9():
    pass


# ex10
def exercise10():
    pass


# ex11
def exercise11():
    pass


# ex12
def exercise12():
    pass


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
