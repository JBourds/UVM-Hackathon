# PROMPT: Reverse an array
from test_case import Test_Case
input = [Test_Case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Test_Case([2, 4, 12, 5, 23, 22, 1, 0]), Test_Case([90, 8, 34, 2])]

def oracle_function(x):
    new_array = x
    return new_array[::-1]

print(oracle_function(input[0]))