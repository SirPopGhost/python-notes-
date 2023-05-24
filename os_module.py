# 1. Import the module
"""
To see and print all the environment variables, use:    
    printenv
To add a new environment variable use: 
    export <name_of_env_var>=<value_of_env_var>
    export TWILLO_SID=1231213
"""
import os

# 2. Create an object of the module or Client of the module
print(f"OS module {os.getcwd()}")
print(f" TWILLO_SID: {os.getenv('TWILLO_SID')}")
