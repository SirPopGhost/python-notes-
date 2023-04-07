"""
Homework 2:
1. Write a program which take two numbers and performs all the math operations.
2. Write a program which takes angle in degrees and find sin, cos and tan for that angle and print it.
3. Write a program which take radius as input and print area of a circle.
4. Write a program which takes length and width for a rectangle and finds and prints its area. Area = 
length * width.
"""
import math

#Homework2: Problem 1
num1 = int(input("Write in a number... "))
num2 = int(input("Write in an another number... "))


print(f"{num1} + {num2}: {num1 + num2}")
print(f"{num1} - {num2}: {num1 - num2}")
print(f"{num1} * {num2}: {num1 * num2}")
print(f"{num1} / {num2}: {num1 / num2}")

#Homework2: Problem 2

degrees = int(input("Put in degrees for your problem "))

print(math.sin(math.radians(degrees)))
print(math.cos(math.radians(degrees)))
print(math.tan(math.radians(degrees)))

#Homework2: Problem 3
radias = int(input("Type in the radius for the area of a circle "))

print(f"A = π{radias}²: {(radias ** 2) * math.pi}")

#Homework2: Problem 4
width = int(input("Write down the width of your rectangle "))
length = int(input("Write down the length of your rectangle "))
print(f"A = {width} * {length}: {width * length}")

#Perfect 