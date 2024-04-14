from test_case import Test_Case

input = [Test_Case((1, "hello", 5)), Test_Case((1,2)), Test_Case((22, "66", 15, False, 5))]


def oracle_function(x):
    total = 0
    count = 0
    for i in range(0, len(x)):
        if type(x[i]) is int:
            total += x[i]
            count += 1
    return total/count

