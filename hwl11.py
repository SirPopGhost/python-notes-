import math

a = 10
b = 20
def sum_of_two(a: int, b: int):
    return a + b

def sub_of_two(a, b):
    total_sub = a - b 
    return total_sub

def mul_of_two(a, b):
    return a * b

def div_of_two(a, b):
    total_add = a / b   
    return total_add

addition = sum_of_two(a, b)
subtract = sub_of_two(a, b)
multiply = mul_of_two(a, b)
divide = div_of_two(a, b)

calculator = 'y'
while calculator == 'y':
    num1 = int(input("Write in a number... "))
    num2 = int(input("Write in an another number... "))
    print(f"{num1} + {num2}: {sum_of_two(num1, num2)}")
    print(f"{num1} - {num2}: {sub_of_two(num1, num2)}")
    print(f"{num1} * {num2}: {mul_of_two(num1, num2)}")
    print(f"{num1} / {num2}: {div_of_two(num1, num2)}")
    calculator = input("Would you like to use the calculator again? y/n ")
print("Bye bye")
