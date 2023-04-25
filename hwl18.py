def write_to_file(output_file):
    with open(output_file, 'w') as file:
        file.write("1, 2, 3, 4, 5, 6, 7, 8, 9, 10")


def main():
    file_name = "numbers.file"
    number_file = write_to_file(file_name)
    print(number_file)
