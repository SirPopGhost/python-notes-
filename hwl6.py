"""
Homework
1. Take grade of 5 students in numbers. Find the max, min, mean(average) print the results.
2. Create an Indian food truck menu. Print the menu for user. Ask users to pick 3 items to order. Give them total.
Add 10% sales tax and ask for that tip. Add the tip to the total and print the final Bill. And say thank you.
"""

indian_market = int(input("Chooose which Indian food you want.. \n 1. Chole bhature $5.99 \n 2. Samosa Chat $2.99 \n 3. Butter Chicken $8.99 \n "))




tax = .1
total = 0 

match indian_market:
   case 1: 
      total = 5.99 + (5.99 * .1)
   case 2:
      total = 2.99 + (2.99 * .1)
   case 3:
      total = 8.99 + (8.99 * .1)
   case _:
      print("Not in menu")
tip = float(input(f"Subtotal is this ${total}, please add in a tip "))
total = total + tip
print(f"${total} \nThank you for coming to the Indian food truck, please come again." )

if total > 1000:
   print("Today in this Mr. Beast video! We are going to tip 1000 dollars to this waiter! ")
elif total > 100:
   print("Oh my god that is so much money!!!! ")