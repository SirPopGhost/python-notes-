import json
from datetime import date

def read_from_file(input_file):
    with open(input_file) as file:
        data_file = file.read()
        json_file = json.loads(data_file)
        return json_file
    
def main():
    birth_dates = "datafile_birthdays.json"
    birth_file = read_from_file(birth_dates)
    today = date.today()
    print(birth_file)
    print(today)

main()

