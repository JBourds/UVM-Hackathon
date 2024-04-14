def user_function(x):
   total = 0
   number_integer = 0
   for element in x:
        if type(element) is int:
            total += element
            number_integer += 1
   return total / number_integer
