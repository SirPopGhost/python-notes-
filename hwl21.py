"""

# Call any covid api from here:
https://covidtracking.com/data/api

Use the api above and get total positive covid test for two distinct dates and print them.

"""
import requests
import json
import hwl20


def main():
    file_name = "covidapi.json"
    response = requests.get(
        "https://api.covidtracking.com/v2/us/daily/2020-12-18/simple.json")
    # api_data = response.json()
    # hwl20.write_to_file("covidapi.json", str(api_data))
    read_data = hwl20.read_from_file(file_name)
    print(read_data.get("data").get("outcomes").get(
        "hospitalized").get("in_icu").get("currently"))

main()

"https://www.flightapi.io"
"https://www.flightapi.io/docs/"