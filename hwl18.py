def write_to_file(output_file, output_file_2):
    with open(output_file, 'w') as file:
        file.writelines(["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n", "8\n", "9\n", "10\n",
                        "11\n", "12\n", "13\n", "14\n", "15\n", "16\n", "17\n", "18\n", "19\n", "20\n"])
    file_name = "numbers.file"
    epic_list = []
    with open(output_file_2, 'w') as file_2:
        first_half, second_half = read_from_file(file_name)
        epic_list = second_half + first_half
        for replacing in epic_list:
            string = str(replacing)
            file_2.writelines(string)
    return

def read_from_file(input_file):
    num1_list = []
    num2_list = []
    with open(input_file, 'r') as file:
        temp_list = file.readlines()
        for replacing in temp_list:
            int_value = int(replacing.replace("\n", ""))
            if int_value % 3 == 0:
                int_value = int_value + 1
                num1_list.append(int_value)
            elif int_value % 10 == 0:
                int_value = int_value - 1
                num2_list.append(int_value)
    return num2_list, num1_list

def main():
    file_name = "numbers.file"
    file_name_2 = "newnumbers.file"
    write_to_file(file_name, file_name_2)

main()
