def are_positive(list_of_nums):
   res = []
   index = 0
   while index < len(list_of_nums):
      if list_of_nums[index] > 0:
         res.append(list_of_nums[index])
      index += 1
   return res

def are_greater_than_n(list_of_nums, n):
   res = []
   index = 0
   for val in list_of_nums:
      if list_of_nums[index] > n:
         res.append(val)
      index += 1
   return res

def are_divisible_by_n(list_of_nums, n):
   return [ val for val in list_of_nums if val % n == 0]
