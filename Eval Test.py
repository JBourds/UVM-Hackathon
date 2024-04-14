from test_case import Test_Case
    
def sum(x,y):
    return x+y

case_1 = Test_Case(1,2)
print(eval(f'sum({case_1.get_arguments()})'))