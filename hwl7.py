a = float(input("Please enter your first grade "))
b = float(input("Please enter your second grade "))
c = float(input("Please enter your third grade "))
d = float(input("Please enter your fourth grade "))
e = float(input("Please enter your fifth grade "))

grades = [a, b, c, d, e]

print(f"The total minimum of your grades ")
print(min(grades))
print("The total maximum of your grades ")
print(max(grades))

total = sum(grades)
mean = len(grades)

print("The average mean of your gradess ")
print(total / mean)
 
 