# Project 3 - Calcudoku Solver
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17

#checks everything
def check_valid(puzzle, cages):
   if check_cages_valid(puzzle, cages) and check_columns_valid(puzzle) and check_rows_valid(puzzle) == True:
      return True
   else:
      return False

def check_cages_valid(puzzle, cages):
   index = 0
   for i in cages:
      if check_one_cage_valid(puzzle, cages, index) == False: 
         return False
      index += 1 
   return True

#checks if given values add up to the given sum_
def check_one_cage_valid(puzzle, cages, index):
   cage = cages[index] 
   indexes = cage[2:]
   sum_ = cage[0]
   sum_of_indexes = 0
   for index in indexes:
      sum_of_indexes += puzzle[index//5][index%5]
   if sum_ == sum_of_indexes and check_cage_for_zeros(puzzle, cages, indexes) == True:
      return True
   elif sum_ != sum_of_indexes and check_cage_for_zeros(puzzle, cages, indexes) == True:
      return False
   elif sum_ <= sum_of_indexes and check_cage_for_zeros(puzzle, cages, indexes) == False:
      return False
   else:
      return True

def check_cage_for_zeros(puzzle, cages, indexes):
   for i in indexes:
      #print(indexes)
      #print(puzzle[i//5][i%5])
      if puzzle[i//5][i%5] == 0:
         return False
   return True




#checks if there are duplicates in columns
def check_columns_valid(puzzle):
   index_4 = 0
   while index_4 < len(puzzle):
      index_3 = 0
      while index_3 < len(puzzle):
         index_2 = 0
         while index_2 < len(puzzle):
            index_1 = 0
            while index_1 < len(puzzle):
               index = 0
               while index < len(puzzle):
                  if puzzle[4][index] == 0:
                     index += 1
                  elif puzzle[4][index] == puzzle[0][index] or puzzle[4][index] ==  puzzle[1][index] or puzzle[4][index] == puzzle[2][index] or puzzle[4][index] == puzzle[3][index]:
                     return False
                  else:
                     index += 1
               if puzzle[3][index_1] == 0:
                  index_1 += 1
               elif puzzle[3][index_1] == puzzle[0][index_1] or puzzle[3][index_1] == puzzle[1][index_1] or puzzle[3][index_1] == puzzle[2][index_1] or puzzle[3][index_1] == puzzle[4][index_1]:
                  return False
               else:
                  index_1 += 1
            if puzzle[2][index_2] == 0:
               index_2 += 1
            elif puzzle[2][index_2] == puzzle[0][index_2] or puzzle[2][index_2] == puzzle[1][index_2] or puzzle[2][index_2] == puzzle[3][index_2] or puzzle[2][index_2] == puzzle[4][index_2]:
               return False
            else:
               index_2 += 1
         if puzzle[1][index_3] == 0:
            index_3 += 1
         elif puzzle[1][index_3] == puzzle[0][index_3] or puzzle[1][index_3] == puzzle[2][index_3] or puzzle[1][index_3] == puzzle[3][index_3] or puzzle[1][index_3] == puzzle[4][index_3]:
            return False
         else:
            index_3 += 1
      if puzzle[4][index_4] == 0:
         index_4 += 1
      elif puzzle[0][index_4] == puzzle[1][index_4] or puzzle[0][index_4] == puzzle[2][index_4] or puzzle[0][index_4] == puzzle[3][index_4] or puzzle[0][index_4] == puzzle[4][index_4]:
         return False
      else:
         index_4 += 1
   return True

#checks if there are duplicates in rows
def check_rows_valid(puzzle):
   index_4 = 0
   while index_4 < len(puzzle):
      index_3 = 0
      while index_3 < len(puzzle):
         index_2 = 0
         while index_2 < len(puzzle):
            index_1 = 0
            while index_1 < len(puzzle):
               index = 0
               while index < len(puzzle):
                  if puzzle[index][4] == 0:
                     index += 1
                  elif puzzle[index][4] == puzzle[index][0] or puzzle[index][4] ==puzzle[index][1] or puzzle[index][4] == puzzle[index][2] or puzzle[index][4] == puzzle[index][3]:  
                     return False
                  else:
                     index += 1
               if puzzle[index_1][3] == 0:
                  index_1 += 1
               elif puzzle[index_1][3] == puzzle[index_1][0] or puzzle[index_1][3] == puzzle[index_1][1] or puzzle[index_1][3] == puzzle[index_1][2] or puzzle[index_1][3] == puzzle[index_1][4]:
                  return False
               else:
                  index_1 += 1
            if puzzle[index_2][2] == 0:
               index_2 += 1
            elif puzzle[index_2][2] == puzzle[index_2][0] or puzzle[index_2][2] == puzzle[index_2][1] or puzzle[index_2][2] == puzzle[index_2][3] or puzzle[index_2][2] == puzzle[index_2][4]:
               return False
            else:
               index_2 += 1
         if puzzle[index_3][1] == 0:
            index_3 += 1
         elif puzzle[index_3][1] == puzzle[index_3][0] or puzzle[index_3][1] == puzzle[index_3][2] or puzzle[index_3][1] == puzzle[index_3][3] or puzzle[index_3][1] == puzzle[index_3][4]:
            return False
         else:
            index_3 += 1
      if puzzle[index_4][0] == 0:
         index_4 += 1
      elif puzzle[index_4][0] == puzzle[index_4][1] or puzzle[index_4][0] == puzzle[index_4][2] or puzzle[index_4][0] == puzzle[index_4][3] or puzzle[index_4][0] == puzzle[index_4][4]:
         return False
      else:
         index_4 += 1
   return True
 
