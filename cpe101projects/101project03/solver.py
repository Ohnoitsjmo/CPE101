# Project 3 - Calcudoku Solver
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17

from solver_funcs import *

def get_cages():
   index = 1
   number_of_cages = int(input("Number of cages: "))
   #print(number_of_cages)
   list_of_entries = list('')
   while index <= number_of_cages:
      cage_number = input(("Cage number {:d}: ".format(index - 1))).split()
      cage_number = [int(a) for a in cage_number]
      list_of_entries.append(cage_number)
      index += 1
   return list_of_entries


def main():
   cages = get_cages()
   #print(cages)
   puzzle = [[0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0]]
   checks = 0
   backtracks = 0
   index_number = 0 
   while index_number < 25:
      if puzzle[index_number//5][index_number%5] == 5:
         puzzle[index_number//5][index_number%5] = 0
         index_number -= 1
         backtracks += 1
         continue
      puzzle[index_number//5][index_number%5] += 1
      checks += 1
      if check_valid(puzzle, cages) == True:
         index_number += 1
         #print(check_valid(puzzle, cages))
         #print("hello")
      else:
         #print("invalid")
         if puzzle[index_number//5][index_number%5] == 5:
            #print("backtracking")
            puzzle[index_number//5][index_number%5] = 0
            index_number -= 1
            backtracks += 1
   print("")
   print("Solution:")
   print("")
   print("{:d} {:d} {:d} {:d} {:d}".format(puzzle[0][0],puzzle[0][1],puzzle[0][2],puzzle[0][3],puzzle[0][4]))
   print("{:d} {:d} {:d} {:d} {:d}".format(puzzle[1][0],puzzle[1][1],puzzle[1][2],puzzle[1][3],puzzle[1][4]))
   print("{:d} {:d} {:d} {:d} {:d}".format(puzzle[2][0],puzzle[2][1],puzzle[2][2],puzzle[2][3],puzzle[2][4]))
   print("{:d} {:d} {:d} {:d} {:d}".format(puzzle[3][0],puzzle[3][1],puzzle[3][2],puzzle[3][3],puzzle[3][4]))
   print("{:d} {:d} {:d} {:d} {:d}".format(puzzle[4][0],puzzle[4][1],puzzle[4][2],puzzle[4][3],puzzle[4][4]))   
   print("")
   print("checks: {:d} backtracks: {:d}".format(checks, backtracks))


if __name__ == '__main__':
   main()
