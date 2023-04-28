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
Step 1: 
Create an input file with 20 random numbers: numbers.txt

Step 2:
#1: if the number is divisible by 3 add 1 to it, 

#2: if number is divisible by 10 sub 1 from it. 
-- Read the numbers from the file, process them using them using logic above, put them in a list
    -- put numbers in different list as per they are going to be written to the file. 
    -- return these two list to main 

Step 3:
Write the results in a new file. Write numbers which were divisible by 10 initially first in file. 
Then Write the numbers initially divisible by 3. 

- in the write function, we are gonna take these two lists as input and write them in the order we want. 
"""

3  -> 4
6  -> 7
10 -> 9
30 -> 29
Result file:
9
29
4
7

4
7
9
29

"""
Your file contains data as below. We are helping the school to put this data into a database. To accomplish this project, 
we want to read the data from the file and put it in a dictionary format. 

Write the resultant dictionary data to a new file.

student_data.txt:

Hint: think of how you can use split, replane, read, readlines, write, writelines
"First_name:Sam;Last_name:Brady;Age:21;School:UCLA;Major:Marketing"
"""