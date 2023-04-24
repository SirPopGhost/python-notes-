"""
Different data file formats:
txt: regular text data file
csv: Comma Seperated Values,
    Ex: sam,bob,James,Rahul,Srikar
JSON: Javascript Object Notation
Binary files, Byte files

To read the data from the file:
https://realpython.com/read-write-files-python/

read: r
write: w
append:

To read from the files:
1. File path should be exactly where the file is located. Ideally keep the file in same folder as code
2. Open the file and assign a file object to work with the file.
3. Use appropriate function to read from the file.


Once you read the file, the file pointer is at the end of the file. So same read function won't read anydata from the file.
"""

"""
A function to read the data from file
"""
def read_from_file(data_file):
    file_data = []
    # Logic to read from the file called data_file
    print(f"Input file is : {data_file}")
    file = open(data_file, 'r')
    # print(f"The result of the read() functions: \n", file.read())
    read_data = file.read()
    print(f"\nread_data has: {read_data}")
    # print(f"The result of the readlines() fucntion: ", {file.readlines()})
    file.close()
    return file_data

def read_lines(data_file):
    # with context, context manager, it will close the file itself
    with open(data_file, 'r') as file:
        print(file.readline(), end="\n\n\n")
        print(file.readlines())
    print("at the end")

def main():
    input_file = "python-notes-/lesson_notes/data.dat"  # Data file is in the same folder as the code, so we don't have to provide entire path to the file
    # read_data = read_from_file(input_file)
    read_data = read_lines(input_file)
    print(f"file contains: {read_data}")
    pass


main()


"""
Homework:
For your data input file: add random integers, example, 
4
89
90
12
45
3
77

Read the data from the files from previous homework using, readlines()
And add 1 to to odd number values and 3 to even number values that you read from the files. 

"""