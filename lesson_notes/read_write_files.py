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
    return file_data


def main():
    input_file = "data.dat"  # Data file is in the same folder as the code, so we don't have to provide entire path to the file
    read_data = read_from_file(input_file)
    print(f"file contains: {read_data}")
    pass


main()


"""
Homework:
1. Make a data.dat, which contains numbers from 1 through 10.
1
2
3
.
.
.
10
Create a function which read the data from the file and puts each line as an element to the list and returns 
the list from the function. 

result: 
[1,2, 3, 4, 5, ..., 10]
['1', '2', '3', '4', ..., '10']

All the function calls should happen within main. Ofc apart from main.

"""