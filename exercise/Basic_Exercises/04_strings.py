# PROMPT: Create a string variable with the value "Hello, World!". Use the len() function to print the length of the string.
from test_case import Test_Case
input = [Test_Case("Tomato"), Test_Case("Banana"), Test_Case("2")]

def oracle_function(x):
    print(len(x))
