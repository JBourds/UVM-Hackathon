from test_case import Test_Case

def double(x: int):
    return 2 * x

def minus_one(x: int):
    return x - 1

input = [Test_Case(double, [1, 3, 4,5]), Test_Case(minus_one, [5,4,5,7,2])]


def oracle_function(f:callable, x: list[int]):
    new_list = []
    for element in x:
        new_list.append(f(element))
    return new_list
