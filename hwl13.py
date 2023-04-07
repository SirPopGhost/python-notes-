'''
Homework:
1. Create a function which find remainder of a % b. Values a and b are parameter of the function.
2. Create a function which takes 3 numbers as inputs and find the biggest and smallest amongst them. Do it both ways using and without using list.
3. Create a function which takes two numbers a and b and prints all the even numbers between them. 
'''
#Homework 12: Problem 1 
def remainder_function(a, b):
    remainder = a % b
    return remainder

print(remainder_function(89, 9))

#Homework 12: Problem 2 
def value():
    number_value = []
    for _ in range(0, 3):
        numbers = int(input("Enter three values.. "))
        number_value.append(numbers)
    hi = max(number_value)
    hello = min(number_value)
    return hi, hello
print(value())

def value2():
    number_value = []
    for _ in range(0, 3):
        numbers = int(input("Enter three values.. "))
        number_value.append(numbers)
    max = number_value[0]
    for highest in number_value:
        if highest > max:
            max = highest
    min = number_value[0]
    for lowest in number_value:
        if lowest < min:
            min = lowest
    return max, min 
print(value2())

#Homework 12: Problem 3 
def even_numbers(a, b):
    a_and_b = []
    for even_numbers in range(a, b + 1):
        if even_numbers % 2 == 0:
            a_and_b.append(even_numbers)
    print(a_and_b)
#Di Molto 






