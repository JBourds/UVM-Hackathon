def user_function(x):
    total = 0
    count = 0
    for i in range(0, len(x)):
        if type(x[i]) is int:
            total += x[i]
            count += 1
    return total / len(x)
