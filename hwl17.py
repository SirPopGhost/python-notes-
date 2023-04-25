def process_file_data(data_file):
    """

    :param data_file:
    :return:
    """
    print(data_file)
    file_list = []
    with open(data_file, 'r') as file:
        file_read = file.readlines()
        for replacing in file_read:
            integer_value = int(replacing.replace("\n", ""))
            if integer_value % 2 == 0:
                file_list.append(integer_value + 3)
            else:
                file_list.append(integer_value + 1)
    return file_list


def write_to_file(output_file, data_to_write):
    """
    Similar to read, we need to open file with correct access, so in this case we will use 'w' to write, when we open the
    file.
    read: 'r'
    write: 'w', this overwrite the existing file. So instead we will append.
    append: 'a'
    read+write: 'r+'

    To write a file:
    1. Open the file
    2. Get a file object
    3. Create the string you want to write to the file.
    4. Use appropriate write function to write.

    """
    with open(output_file,'w') as file:
        file.write("Hello this is your first line.\n")
        file.writelines(["Hello\n", "4\n"])
        file.write(str(data_to_write))
        file.writelines(str(data_to_write))


def main():
    """

    :return:
    """
    file_name = "randomnumbers.file"
    data_file = process_file_data(file_name)
    print(data_file)
    write_to_file("dummy_output.txt", data_file)


main()

"""
Create a file with 20 random numbers, 
#1: if the number is divisible by 3 add 1 to it, 

#2: if number is divisible by 10 sub 1 from it. 

Write the results in a new file. Write numbers which were divisible by 10 initially first in file. 
Then Write the numbers initially divisible by 3. 
"""