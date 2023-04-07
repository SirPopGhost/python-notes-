"""""
Homework:
Create a list of 10 elements all numbers:
1. Find the average of elements at the odd indexes and Find minimum from all the elements at the even indexes.
2. Take a string from user as input and reverse the input string and print it. Do not use reverse function.
Hint: Think list negative indexes
3. Make a list 5 names of sci-fi characters. Add two more names at the end of the list without coping it.
- Remove the first name from the list
- Add a name in middle of the list.
"""""

#Homework 8: Problem 1
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
average_odd_list = sum(list[0::2])
total_odd_list = len(list[0::2])
print(f"The average of the odd indexes list: {average_odd_list / total_odd_list}")
print(f"Minimum of the even indexes list: {min(list[1::2])}")

#Homework 8: Problem 2
string = input("Enter a random string ")
print(f"The string backwards is! {string[-1::-1]}" )

#Homework 8: Problem 3
sci_fi_characters = ["Malcom Reynolds", "Spock, The Doctor", "Boba Fett", "Darth Vader", "RD-D2"]
print(f"Science fiction characters: {sci_fi_characters}" )
one = sci_fi_characters[0]  
two = sci_fi_characters[1]
three = sci_fi_characters[2]
four = sci_fi_characters[3]
five = sci_fi_characters[4]
six = "Yoda"
seven = "Q"



more_characters = [one, two, three, four, five, six, seven]
print(f"Additional science fiction characters: {more_characters}")
print(more_characters[1:])

four_point_five = "BB-8"
more_characters2 = [one, two, three, four, four_point_five, five, six, seven]
print(more_characters2)

#Di Molto