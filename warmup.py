# read the data from the file
# process read data
# find the age of the youngest person
import json

def read_from_file(data_file):
    with open(data_file, 'r') as file:
        file_data = file.read() 
        list_file = file_data.split('\n\n')
    return list_file

def writ_to_file(output_file, dict_list):
    with open(output_file, 'w') as result_file:
        json_data = json.dumps(dict_list)
        result_file.write(json_data)

def list_to_dict(list_data):
#    print(f"This is the list data: {list_data}.")
    dict_list = []
    for conv_list in list_data:
        split_list = conv_list.split("\n")
        student_dict = {}
#        print(f"This is splist list: {split_list}")
        for splitting in split_list:
            split_values = splitting.split(": ")
            student_dict[split_values[0]] = split_values[1]
        dict_list.append(student_dict)
    return dict_list

def dict_conv(output_file):
    with open(output_file, 'r') as dict_file:
        read_file = dict_file.read()
        dict_list = json.loads(read_file)
        return dict_list

def ind_search(list_data, profile_name):
    for search_list in list_data:
        if search_list.get("Name") == profile_name:
            print(search_list.get("Interests"))
            break
    else:
        print("This user does not exist.")

        
def main():
    file_name = "Data.txt"
    read_file = read_from_file(file_name)
    dict_data = list_to_dict(read_file)
    writ_to_file("warmup_file.json", dict_data)
    list_dict = dict_conv("warmup_file.json")
    user_input = input("Enter username you want to find. ")
    ind_search(list_dict, user_input)
main()

"""
Homework:
Extract the split data into a key:value pair and make a dictionary for each of the person.
The function should return a list of dictionary and, each of the element in the list will be an individual dictionary representing each of the person. 
"""