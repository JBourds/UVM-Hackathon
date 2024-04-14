def user_function(x):
    new_list = []
    for i in range(0, len(x)):
        new_list.append(x[len(x) - (i + 1)])
    return new_list
