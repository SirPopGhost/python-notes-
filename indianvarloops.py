'''
Create an Indian food truck menu. Print the menu for user. Ask users to pick 5 items from the menu. Ask user if they want to order more and give them an option to order more. 
Give them total.
Add 10% sales tax and ask for that tip. Add the tip to the total and print the final Bill. And say thank you.
'''
# order = int(input(("Here is the menu:\n1.Chicken Briyani 5.99$\n2.Butter Chicken 6.99$\n3.Samosa Chat $4.99\n4.Poori $4.99\n5.Pav bhaji $6.99\n")))
menu = ("1.Chicken Briyani 5.99$\n2.Butter Chicken 6.99$\n3.Samosa Chat $4.99\n4.Poori $4.99\n5.Pav bhaji $6.99\n")
# match order:
#    case 1: 
#       total = 5.99 + (5.99 * .1)
#    case 2:
#       total = 6.99 + (6.99 * .1)
#    case 3:
#       total = 4.99 + (4.99 * .1)
#    case 4:
#       total = 4.99 + (4.99 * .1)
#    case 5:
#       total =  6.99 + (6.99 * .1)
#    case _:
#       print("Not in menu")
total = 0 
user_choice = "y"
while user_choice == "y":
    order = int(input(menu))
    user_choice = input("Are you interested in buying more? y/n ")
    match order:
        case 1: 
            sub_total = 5.99 + (5.99 * .1)
        case 2:
            sub_total = 6.99 + (6.99 * .1)
        case 3:
            sub_total = 4.99 + (4.99 * .1)
        case 4:
            sub_total = 4.99 + (4.99 * .1)
        case 5:
            sub_total =  6.99 + (6.99 * .1)
        case _:
            print("Not in menu")
    total = sub_total + total
total = total * .105 + total
tip = float(input(f"Total is: ${total}. Please add an tip for our service "))
total = total + tip
print(f"${total}\nThank you for coming to our Indian food shop, please come again.")