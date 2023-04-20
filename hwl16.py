def data_from_file(data_file):
    data_list = []
    file = open(data_file, 'r')
    read_data = file.read()
    data_list.append(read_data)
    return data_list

def main():
    input_file = "data.dat"
    read_data = data_from_file(input_file)
    return read_data

print(main())