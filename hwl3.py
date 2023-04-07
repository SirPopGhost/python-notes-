"""""
Homework:
1. Take two float type values from user, find the floor value of the first float and
ceiling value of the second float and print the results.
Hint: Use Math library function
2. Rewrite finding area of a circle using float type value for the radius of the circle.
3. Take one a number as input from the user and print it's int, float and boolean conversion.
Note: You might run into errors so do this one last at the end of the file.
4. Add % operator to the previous calculator(Homework 2 first problem)
"""
import math
#Homework2: Problem 1

float_value_one = float(input("Enter a float value "))


float_value_two = float(input("Enter the second float value "))

print(f"First floor and ceiling value of {float_value_one} is: {math.floor(float_value_one)} and {math.ceil(float_value_one)}" )

print(f"The next floor and ceiling value of {float_value_two} is: {math.floor(float_value_two)} and {math.ceil(float_value_two)}" )

#Homework2: Problem 2

radias = float(input("Type in the radius for the area of a circle "))

print(f"A = π{radias}²: {(radias ** 2) * math.pi}")

#Homework2: Problem 4

num1 = int(input("Write in a number... "))
num2 = int(input("Write in an another number... "))

print(f"Remainder of {num1} and {num2}: {num1%num2}" )

#Homework2: Problem 3
special_number = input("Write in any number ")
print(f"Integer value: {int(special_number)}")
print(f"Float value: {float(special_number)}")
print(f"Boolean value: {bool(special_number)}")

print(int(23.99))
#Di Molto 
4