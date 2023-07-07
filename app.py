import json
import datetime

def read_from_file(input_file):
    with open(input_file) as file:
        data_file = file.read()
        json_file = json.loads(data_file)
        return json_file

def birthday_finder(date_data, data_file):
    birthday_list = []
    month = date_data.month
    day = date_data.day
    month = str(month)  
    day = str(day)
    date = (f"{month}-{day}")
    for birthdays in data_file:
        birth_file = birthdays.get("birthdate")
        if birth_file == date:
            birthday_list.append(birth_file)
    print(birthday_list)


def main():
    birth_dates = "datafile_birthdays.json"
    birth_file = read_from_file(birth_dates)
    current_time = datetime.datetime.now()
    birthday_finder(current_time, birth_file)
    




main()

