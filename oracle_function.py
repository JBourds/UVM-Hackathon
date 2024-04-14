# PROMPT: Using a for loop, take x, a list of numbers and add 1 to each number. return the new list.

input = [([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2), ([2, 4, 12, 5, 23, 22, 1, 0], 3), ([90, 8, 34, 2], 4)]

def oracle_function(tuple_containing_x_y):
    new_array = []
    x = tuple_containing_x_y[0]
    y = tuple_containing_x_y[1]
    for i in range(0, len(x)):
        new_array.append(x[i] * y)
    return new_array