"""
Homework:
1. Optimize previous homework answer. Instead of 5 individual input for grades, take 15 different grade from user.
2. Add odd numbers between 1-23 in a list, not manually adding them to the list and find min and max on that list. With out using library functions.
3. Find total of all the numbers divisible by 3 between 333-400 without using library functions.
"""
#Problem 1
score_list = []

for user_input in range(1, 6):
    score = float(input("Enter your grades.. "))
    score_list.append(score)

print(score_list)

max = score_list[0]
for current_value in score_list:
    if current_value > max:
        max = current_value
print(max)

max = score_list[0]
for current_value in score_list:
    if current_value > max:
        current_value = max
print(current_value)
print(score_list)

#Problem 2
a_list = []

for numbers in range(1, 24):
    if numbers % 2 != 0:
        a_list.append(numbers)
print(a_list)

min = a_list[0]
for current_value in a_list:
    if current_value < min:
        min = current_value
print(min)

#Problem 3 
div_three = []
for umbers in range(333, 401):
    if umbers % 3 == 0:
        div_three.append(umbers)

total = 0
for adding in div_three:
    total = adding + total
print(total)
