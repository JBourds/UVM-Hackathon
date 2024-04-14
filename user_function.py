def user_function(x:list,y: int):
   new_list = []
   for i in range(1, len(x)):
        new_list.append(x[i] * y)
   return new_list