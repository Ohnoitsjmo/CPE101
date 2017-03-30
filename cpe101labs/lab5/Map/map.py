def square_all(list_of_nums):
   return[value**2 for value in list_of_nums]

def add_n_all(list_of_nums, n):
   res = []
   for val in list_of_nums:
      res.append(val + n)
   return res

def even_or_odd_all(list_of_nums):
   res = []
   index = 0
   while index < len(list_of_nums):
      res.append(list_of_nums[index] % 2 == 0)
      index += 1 
   return res
