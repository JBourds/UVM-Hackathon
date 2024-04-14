# PROMPT: Using a for loop, take x, a list of numbers and add 1 to each number. return the new list.
from test_case import Test_Case

case_1 = Test_Case([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [5,4,7,2,1,6,3,5,7,1])
case_2 = Test_Case([2, 4, 12, 5, 23, 22, 1, 0],[3,8,55,4,33,2,7,4])
case_3 = Test_Case([90, 8, 34, 2], [54, 7, 43, 1])
case_4 = Test_Case(["Hello", "Name", "Spencer"], ["My", "Is", "Brouhard"])
input = [case_1, case_2, case_3, case_4]

def oracle_function(x: list,y: list):
    new_list = []
    for i in range(0, len(x)):
        new_list.append(x[i])
        new_list.append(y[i])
    return new_list

