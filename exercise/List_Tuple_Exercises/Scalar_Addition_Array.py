# PROMPT: Using a for loop, take x, a list of numbers and add 1 to each number. return the new list.
from test_case import Test_Case
input = [Test_Case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), Test_Case([2, 4, 12, 5, 23, 22, 1, 0]), Test_Case([90, 8, 34, 2])]

def oracle_function(x):
    new_array = []
    for i in range(0, len(x)):
        new_array.append(x[i] + 1)
    return new_array
