
# PROMT: Now try creating a variable that contains "Hello, World!" and print it by printing the variable.
from test_case import Test_Case
cases = []
for i in range(0, 4):
    cases.append(Test_Case(i))
input = cases

def oracle_function(x):
    total = 0
    for i in range(0, x):
        total += i
    return total
