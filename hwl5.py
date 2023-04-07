"""
Homework:
1. Take a number from the user, find if that number is odd or even
Hint: Look up how to find odd or even
2. Take two numbers from the user, check if the smaller number between them and print the same if they are 
the same.
3. Update grading calculator from last homework using and, or operator.
"""

#Homework 5: Problem 1
randomnum = int(input("Enter a number.. ")) 

if randomnum % 2 == 0:
    print(f"{randomnum} an even number ")
else:
    print(f"{randomnum} is an odd number ")

#Homework 5: Problem 2
num1 = int(input("Enter the first number "))
num2 = int(input("Enter the second number "))

if num1 > num2:
    print(f"{num1} is greater than {num2} ")
elif num1 < num2:
    print(f"{num1} is lesser than {num2} ")
else:
    print(f"{num1} and {num2} are equal.")

#Homework 5: Problem 3
grade = float(input("Put in your grade "))

if grade >= 0 and grade < 60:
    print("F grade ")
elif grade >= 60 and grade <= 63:
    print("Grade D- ")
elif grade > 63 and grade < 67:
    print("D grade ")
elif grade >= 67 and grade <= 70:
    print("D+ grade ")
elif grade >= 70 and grade <= 73:
    print("Grade C- ")
elif grade > 73 and grade < 77:
    print("C grade ")
elif grade >= 77 and grade < 80:
    print("C+ grade ")
elif grade >= 80 and grade <= 83:
    print("Grade B- ")
elif grade > 83 and grade < 87:
    print("B grade ")
elif grade >= 87 and grade <= 90:
    print("B+ grade ")
elif grade >= 90 and grade <= 93:
    print("Grade A- ")
elif grade > 93 and grade < 97:
    print("Grade A ")
elif grade >= 97 and grade <= 100:
    print("Grade A+")
else: 
    print("Not in value ")  

#Perfect