from test_case import Test_Case

input = [Test_Case("Banana"), Test_Case("racecar"), Test_Case(""), Test_Case("tomato"), Test_Case("spencer")]

def oracle_function(x):
    new_string = ""
    for i in range(0, len(x)):
        new_string += x[len(x)- (i + 1)]
    return new_string
