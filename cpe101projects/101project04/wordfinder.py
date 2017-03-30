# Project 4
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17
from finder_funcs import *

def main():
   puzzle_string = str(input(""))
   words = str(input(""))
   interval = 10
   list_of_rows = [puzzle_string[i:i+interval] for i in range(0, len(puzzle_string), interval)]
   print("Puzzle:")
   print("")
   print(list_of_rows[0])
   print(list_of_rows[1])
   print(list_of_rows[2])
   print(list_of_rows[3])
   print(list_of_rows[4])
   print(list_of_rows[5])
   print(list_of_rows[6])
   print(list_of_rows[7])
   print(list_of_rows[8])
   print(list_of_rows[9])
   print("") 
   finder = multiple_word_finder(puzzle_string, words)













if __name__ == '__main__':
   main()
