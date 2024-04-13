import json
import os 
import contextlib
from io import StringIO

# This will be database Access
problem_id = 1
oracle_function = "def oracle_function(x):\n\ttotal = 0\n\tfor i in range(0,x):\n\t\ttotal += 2 * i\n\treturn total"
test_values = [0, 1, 2, 4]


# Writing oracle function to oracle_function.py
file2 = open("oracle_function.py", "w")
file2.write(oracle_function)
file2.close()

from oracle_function import oracle_function



# Reading in functon from user_input.json
f = open('user_input.json')
user_input = json.load(f)
f.close()

# Getting function as string from user_input.json and writing it to user_function.py
user_function = user_input["user_function"]
file2 = open("user_function.py", "w")
file2.write(user_function)
file2.close()







user_function_output = {}
oracle_function_output = {}


try:
    from user_function import user_function

    if test_values == []:
                result = user_function()
                oracle_result = oracle_function()
    for value in test_values:    
        result = user_function(value)
        oracle_result = oracle_function(value)
        user_function_output[value] = result
        oracle_function_output[value] = oracle_result
    print()
    for key in user_function_output.keys():
         if user_function_output[key] != oracle_function_output[key]:
              print(f'Test case with input {key} failed: Correct answer is {oracle_function_output[key]} and user answer is {user_function_output[key]}')
    print()
    print()
    print(user_function_output)
    print(oracle_function_output)


           
except Exception as e: 
    print(e)
    print("Code does not run")


