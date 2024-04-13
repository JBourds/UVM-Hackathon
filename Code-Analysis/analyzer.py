import json
import os 
import contextlib
import pprint
from gpt import GPT_CLIENT



from io import StringIO 
import sys
import pickle
import os
from dotenv import load_dotenv


def analyze_code(user_input_dictionary):
    load_dotenv()
    class Capturing(list):
        def __enter__(self):
            self._stdout = sys.stdout
            sys.stdout = self._stringio = StringIO()
            return self
        def __exit__(self, *args):
            self.extend(self._stringio.getvalue().splitlines())
            del self._stringio    # free up some memory
            sys.stdout = self._stdout

    # This will be database Access
    problem_id = 1
    oracle_function_string = "def oracle_function(x):\n\t print(f'{2 * x}')"
    test_values = [0, 1, 2, 4]
    prompt = "Please write a function which takes in a parameter x and prints 2 times the parameter"


    # Writing oracle function to oracle_function.py
    file2 = open("oracle_function.py", "w")
    file2.write(oracle_function_string)
    file2.close()

    from oracle_function import oracle_function




    # Getting function as string from user_input.json and writing it to user_function.py
    user_function_string = user_input_dictionary["user_function"]
    file2 = open("user_function.py", "w")
    file2.write(user_function_string)
    file2.close()







    user_function_output = {}
    oracle_function_output = {}


    try:
        from user_function import user_function

        if test_values == []:
                    result = user_function()
                    oracle_result = oracle_function()
        for value in test_values:    
            with Capturing() as out_oracle:
                result = oracle_function(value)
                if result is not None:
                    print(result)
            with Capturing() as out_user:
                result = user_function(value)
                if result is not None:
                    print(result)    

            user_function_output[value] = out_user
            oracle_function_output[value] = out_oracle

        failed_comparison = False
        for key in user_function_output.keys():
            if user_function_output[key] != oracle_function_output[key]:
                failed_comparison = True
                print(f'Test case with input {key} failed: Correct answer is {oracle_function_output[key]} and user answer is {user_function_output[key]}')
        print()
        print("USER FUNCTION:")
        print(user_function_string)
        print("ORACLE FUNCTION:")
        print(oracle_function_string)
        print()
        if failed_comparison:
            gpt_client = GPT_CLIENT(oracle_function_string, user_function_string, oracle_function_output, user_function_output, prompt)
            gpt_response = gpt_client.send_request().content
        
        return {"Expected_IO" : oracle_function_output, "Actual_IO": user_function_output, "GPT_HELP": gpt_response}

    except Exception as e: 
        return {"response": "code failed to run"}

    


user_input_dictionary = {
    "problem_id": 1,
    "user_function":
        "def user_function(x): \n\t print(f'{x}')"
}

output_dict = analyze_code(user_input_dictionary)
print(json.dumps(output_dict, indent=4))