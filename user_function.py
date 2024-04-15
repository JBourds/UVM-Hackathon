
def user_function(f:callable, x: list[int]):
    new_list = []
    for element in x:
        new_list.append(double(element))
    return new_list
