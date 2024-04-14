def user_function(tuple_containing_x_y):
    x = tuple_containing_x_y[0]
    y = tuple_containing_x_y[0]
    new_array = []
    for element in x:
        new_array.append(element * y)
    return new_array