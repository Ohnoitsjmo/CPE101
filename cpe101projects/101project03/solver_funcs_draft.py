# Project 3 - Calcudoku Solver
#
# Name: <Your name here>
# Instructor: Brian Jones
# Section: 17 

def check_valid(puzzle, cages):
   if check_cages_valid(puzzle, cages) and check_columns_valid(puzzle) and check_rows_valid(puzzle) == True:
      return True 
   else: 
      return False

def create_cages(number_of_cages):
   index = 0
   while number_of_cages < cages[index]:
      index += 1 

def check_cages_valid(puzzle, cages):
   index = 0
   while index < len(cages):
      if cages[index][1] + 2 == len(cages[index]):
         sum_ = 0
         for each_values_add in cages[2:len(cages[index]) + 1]:
            string_each_values = ''.join(str(e) for e in each_values_add)
            sum_ = sum_ + int(string_each_values)
            index += 1
            if cages[index][0] == sum_:
               return True
            else: 
               return False
            
def cages_sum(puzzle, cages):
   index = 0
   value = 2
   while index < len(cages):
      '5' == 0
      '6' == 1
      '7' == 2
      '8' == 3
      '9' == 4
      '10' == 0
      '11' == 1
      '12' == 2
      '13' == 3
      '14' == 4
      '15' == 0
      '16' == 1
      '17' == 2
      '18' == 3
      '19' == 4
      '20' == 0 
      '21' == 1
      '22' == 2
      '23' == 3
      '24' == 4
      for i in range(2, cages[index][len(cages[index])] + 1):
         cages[index][value] = puzzle[index][value]
         index += 1
         value += 1

def check_columns_valid(puzzle): 

   index = 0
   while index < len(puzzle):
      while index < len(puzzle):
         while index < len(puzzle):
            while index < len(puzzle):
               while index < len(puzzle):
                  if puzzle[4][index] != puzzle[0][index] or puzzle[1][index] or puzzle[2][index] or puzzle[3][index]:
                     index +=1
               if puzzle[3][index] != puzzle[0][index] or puzzle[1][index] or puzzle[2][index] or puzzle[4][index]:
                  index += 1 
            if puzzle[2][index] != puzzle[0][index] or puzzle[1][index] or puzzle[3][index] or puzzle[4][index]:
               index += 1
         if puzzle[1][index] != puzzle[0][index] or puzzle[2][index] or puzzle[3][index] or puzzle[4][index]:
            index += 1
      if puzzle[0][index] != puzzle[1][index] or puzzle[2][index] or puzzle[3][index] or puzzle[4][index]:
         index += 1
      return True
   return False
         
        
         while index < len(puzzle):  
            if puzzle[1][index] != puzzle[0][index] or puzzle[2][index] or puzzle[3][index] or puzzle[4][index]:
               index += 1
             
               while index < len(puzzle):
                  if puzzle[2][index] != puzzle[0][index] or puzzle[1][index] or puzzle[3][index] or puzzle[4][index]:
                     index += 1
               
                  while index < len(puzzle):
                     if puzzle[3][index] != puzzle[0][index] or puzzle[1][index] or puzzle[2][index] or puzzle[4][index]:
                        index += 1
                  
                        while index < len(puzzle):
                           if puzzle[4][index] != puzzle[0][index] or puzzle[1][index] or puzzle[2][index] or puzzle[3][index]:
                              index +=1   
                               

def check_rows_valid(puzzle):
   index = 0
   while index < len(puzzle):
      while index < len(puzzle):
         while index < len(puzzle):
            while index < len(puzzle):
               while index < len(puzzle):
                   if puzzle[index][4] != puzzle[index][0] or puzzle[index][1] or puzzle[index][2] or puzzle[index][3]:
                      index += 1
               if puzzle[index][3] != puzzle[index][0] or puzzle[index][1] or puzzle[index][2] or puzzle[index][4]:
                  index += 1
            if puzzle[index][2] != puzzle[index][0] or puzzle[index][1] or puzzle[index][3] or puzzle[index][4]:
               index += 1
         if puzzle[index][1] != puzzle[index][0] or puzzle[index][2] or puzzle[index][3] or puzzle[index][4]:
            index += 1
      if puzzle[index][0] != puzzle[index][1] or puzzle[index][2] or puzzle[index][3] or puzzle[index][4]:
         index += 1
      return True
   return False

      if puzzle[index][0] != puzzle[index][1] or puzzle[index][2] or puzzle[index][3] or puzzle[index][4]: 
         if puzzle[index][1] != puzzle[index][0] or puzzle[index][2] or puzzle[index][3] or puzzle[index][4]:
            if puzzle[index][2] != puzzle[index][0] or puzzle[index][1] or puzzle[index][3] or puzzle[index][4]:
               if puzzle[index][3] != puzzle[index][0] or puzzle[index][1] or puzzle[index][2] or puzzle[index][4]:  
                  if puzzle[index][4] != puzzle[index][0] or puzzle[index][1] or puzzle[index][2] or puzzle[index][3]:
                        index += 1
                        return True
      else:
         return False 
           
