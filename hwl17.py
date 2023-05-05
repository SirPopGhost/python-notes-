def process_file_data(data_file):
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


def main():
    file_name = "randomnumbers.file"
    data_file = process_file_data(file_name)
    print(data_file)


main()