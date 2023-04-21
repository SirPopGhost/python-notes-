def data_from_file(data_file):
    result_list = []
    file = open(data_file, 'r')
    read_data = file.read()
    data_list = read_data.split('\n')
    for integer in data_list:
        integer_list = int(integer)
        result_list.append(integer_list)
    return result_list

def main():
    input_file = "data.dat"
    read_data = data_from_file(input_file)
    print(read_data)

main()