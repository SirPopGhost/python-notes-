"""
Homework:
1. Create a function which takes length and width of the triangle and finds its area.
2. Create a function which asks user to enter angle in degrees and converts it to radians and prints its sin and cos values.
3. Create a function which takes an integer variable called counter and called above two functions that many times.
"""
import math
# Homework 12 Problem 1


def area_of_triangle():
    length = int(input("Please enter height "))
    height = int(input("Please enter length "))
    return length * height * 0.5

def area_of_circle():
    rad = int(input("Please enter radius 3"))
    return 3.14 * rad * rad
print(area_of_circle())


def useful_trig_functions():
    angle = float(input("Please enter in a degree "))
    radians = float(input("Please enter in radians "))
    radian_sin = math.sin(math.radians(angle))
    raidan_tan = math.atan(math.radians(radians))
    return radian_sin, raidan_tan


def function_caller(counter):
    for _ in range(1, counter + 1):
        print(area_of_triangle())
        print(useful_trig_functions())




# number = int(input("Enter a number "))
# function_caller(number)


