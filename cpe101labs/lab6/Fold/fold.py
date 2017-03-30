def sum(list_of_nums):
  index = 0
  sum = 0
  while index < len(list_of_nums):
     sum += list_of_nums[index] 
     index += 1
  return sum

def index_of_smallest(list_of_nums):
 if len(list_of_nums) > 0:
    return list_of_nums.index(min(list_of_nums))
 else:
    return -1


   
