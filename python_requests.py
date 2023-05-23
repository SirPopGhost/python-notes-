"""
API: Application programming Interface
This connects your(Developer) data to the front-end/


"your data in the database(Your database)" -> Application  -> USER
API - Connects data to the user, a way to provide access to the data or database

REST API:
request module
- simply a way to get to a website or database using command line/code
- request: CRUD -> Create Read Update Delete

post to Create
get to get information - Read
put to Update
delete to delete

request module send a request to the server in 4 forms: get, post, put, delete
endpoint aka API  aka URL

API returns HTTP status code:
either in
200 - All good
400 - 401, 404- Not found, "You messed"
500 - 501 server too busy, 503 - bad gateway- "The server messed up"
"""
import requests
import math
import hwl20

try:
    response = requests.get("https://api.covidtracking.com",data={'name': 'sam'})
    print(f"API returned: {response.json()}")
    json_data = response.json()
except Exception as e:
    print(f"Error: {e} happened while calling the api.")

try:
    x = 1/0
except ZeroDivisionError as e:
    print(e)
# hwl20.write_to_file("events.json", str(json_data))




"""

# Call any covid api from here:
https://covidtracking.com/data/api

Use the api above and get total positive covid test for two distinct dates and print them.

"""
