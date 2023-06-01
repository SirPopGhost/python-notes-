import json
import datetime

def read_from_file(input_file):
    with open(input_file) as file:
        data_file = file.read()
        json_file = json.loads(data_file)
        return json_file
    


def main():
    birth_dates = "datafile_birthdays.json"
    birth_file = read_from_file(birth_dates)
    current_time = datetime.datetime.now()
    print(birth_file)
    month = current_time.month
    day = current_time.day
    print(type(month), type(day))


main()

