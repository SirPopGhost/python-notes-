"""
Homework:
1. Take a list 10 grades, Add one to each of the grade and print the new values for each. Print each value one by one.
2. Take a list of 10 numbers, print if the given element is even or odd. Based on its value and print a statement saying
its even or odd.


Extra:
Take user input of their 5 grades. Find its min, max and average without using list library functions.
Now 3 students dropped out from that class. Find the new min, max and average without using list library functions.
"""
#Homework 9: Problem 1 
import math
grades = [10, 20.23, 42, 23.45, 50.68, 77.77, 89.89, 85, 99, 100]

for value in grades:
    print(type(value))

#Homework 10: Problem 2
for odd_or_even in grades:
    if odd_or_even % 2 == 0:
        print("Even")
    else:
        print("Odd")

#Homework 10: Extra
first_grade = float(input("Put in your first grade.. "))
second_grade = float(input("Put in your second grade.. "))
third_grade = float(input("Put in your third grade.. "))
fourth_grade = float(input("Put in your fourth grade.. "))
fifth_grade = float(input("Put in your fifth grade.. "))

grades = [first_grade, second_grade, third_grade, fourth_grade, fifth_grade]


print(f"Total minimum grades: {min(grades)}")
print(f"Total maximum grades: {max(grades)}")

total_grades = first_grade + second_grade + third_grade + fourth_grade + fifth_grade
print(f"Average amount of grades: {total_grades / 5}")

new_grade = first_grade
second_new_grade = second_grade
next_grades = [new_grade, second_grade]
print(f"Minimum grades after three students dropped out: {min(next_grades)}")
print(f"Minimum grades after three students dropped out: {max(next_grades)}")

total_next_grades = new_grade + second_new_grade 
print(f"Average amount of grades after three students dropped out: {total_next_grades / 2}")

#Di Molto 
