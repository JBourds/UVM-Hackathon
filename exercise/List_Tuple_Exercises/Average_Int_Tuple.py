from test_case import Test_Case


input = [Test_Case((1, 3, 5)), Test_Case((1,2)), Test_Case((22, 66, 15, 52, 5))]

def oracle_function(x):
    total = 0
    for i in range(len(x)):
        total += x[i]
    return total/len(x)
