"""
Your file contains data as below. We are helping the school to put this data into a database. To accomplish this project, 
we want to read the data from the file and put it in a dictionary format. 
Write the resultant dictionary data to a new file.
student_data.txt:
Hint: think of how you can use split, replane, read, readlines, write, writelines
"First_name:Sam;Last_name:Brady;Age:21;School:UCLA;Major:Marketing"
"""
import json

def read_from_file(input_file): 
    student_dict = {}
    with open(input_file, 'r') as file:
        data_file = file.read()
        data_list = data_file.split(";")
        for replacing in data_list:
            key_value_pairs = replacing.split(":")
            key = key_value_pairs[0]
            value = key_value_pairs[1]
            student_dict[key] = value
    return student_dict
            

def write_to_file(output_file, data):
    with open(output_file, 'w') as file:
        file.write(json.dumps(data))

def read_test(input_file):
    with open(input_file, 'r') as file:
        data = file.read()
        json_file = json.loads(data)
        return json_file


def main():
    file_name = "student_data.txt"
    file_name_2 = 'student_dict.json'
    student_dict = read_from_file(file_name)
    write_to_file(file_name_2, student_dict)
    read_file = read_test(file_name_2)
    print(type(read_file))
    
main()