# Project 3 - Calcudoku Solver
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17

from solver_funcs import *

def get_cages():
   index = 1
   number_of_cages = int(input("Number of cages: "))
   list_of_entries = list('')
   if number_of_cages == 0:
      return 0
   else:
      while index <= number_of_cages:
         cage_number = input("Cage number {:d}: ".format(index - 1))
         cage_number = [int(a) for a in cage_number.split()]
         list_of_entries.append(cage_number)
         index += 1
      return list_of_entries

def main():
   cages = get_cages()
   puzzle = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
   checks = 0
   backtracks = 0
   index = 0
   inner_index = 0
   value = 1
   while index < 5:
      value = 1
      inner_index = 0
      while inner_index < 5:
         puzzle[index][inner_index] = value
         while value < 5:
            print(value)
            if check_valid(puzzle, cages) == True:
               inner_index += 1
               value = 1
               checks += 1             
            if check_columns_valid(puzzle) == False or check_rows_valid(puzzle) == False:
               value += 1
               checks += 1
               print("hehe xd")
         if value < 5 and check_cages_valid_2(puzzle, cages) == False and check_cages_valid(puzzle, cages) == True:
            if inner_index == 0:
               value = 0
               index -= 1
               inner_index = 4
               backtracks += 1
               print("hi")
            else:
               value += 1
               inner_index -= 1
               backtracks += 1
               print("lol")
         if value > 5: 
            if inner_index == 0:
               value = 0
               index -= 1
               inner_index = 4
               backtracks += 1
               value += 1
               print("hey")
            else:
               value = 0
               inner_index -= 1
               value += 1
               backtracks += 1
               print("yo")
      index += 1
   print("")
   print("Solution:")
   print("")
   print(puzzle[0])
   print(puzzle[1])
   print(puzzle[2])
   print(puzzle[3])
   print(puzzle[4])
   print("")
   print("checks: {:d} backtracks: {:d}".format(checks, backtracks))


if __name__ == '__main__':
   main()

