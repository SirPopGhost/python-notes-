"""
How to format you source code:
Divide the source code in the logical blocks.
blocks such as data, functions, main function and so on...

main function - is the starting point of the program.
It is simple another function mostly without any parameters.
It simply decided the flow of the program and has bunch of function calls.
"""


# function definitions
def sum_of_two(num1, num2):
    return num1 + num2


def main():
    # Data section
    num1 = 50
    num2 = 78

    # Flow of the logic or Function Calls
    result = sum_of_two(num1, num2)
    print(result)


# Call the main function
main()