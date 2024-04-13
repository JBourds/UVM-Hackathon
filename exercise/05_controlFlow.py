# PROMPT: Using a for loop, take x, a list of numbers and add 1 to each number. return the new list.

input = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [2, 4, 12, 5, 23, 22, 1, 0], [90, 8, 34, 2]]

def oracle_function(x):
    for i in range(len(x)):
        x[i] += 1

    return x
