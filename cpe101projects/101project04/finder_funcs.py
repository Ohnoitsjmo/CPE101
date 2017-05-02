# Project 4
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17

def get_rows(puzzle_string):
   interval = 10
   list_of_rows = [puzzle_string[i:i+interval] for i in range(0, len(puzzle_string), interval)]
   return list_of_rows

def get_reverse_rows(puzzle_string):
   interval = 10
   reverse_string = puzzle_string[::-1]
   reverse_list_of_rows = [reverse_string[i:i+interval] for i in range(0, len(reverse_string), interval)]
   return reverse_list_of_rows
 
def get_columns(puzzle_string):
   interval = 10
   column_1 = puzzle_string[::10] 
   column_2 = puzzle_string[1::10]
   column_3 = puzzle_string[2::10]
   column_4 = puzzle_string[3::10]
   column_5 = puzzle_string[4::10]
   column_6 = puzzle_string[5::10]
   column_7 = puzzle_string[6::10]
   column_8 = puzzle_string[7::10]
   column_9 = puzzle_string[8::10]
   column_10 = puzzle_string[9::10]
   string_of_columns = column_1 + column_2 + column_3 + column_4 + column_5 + column_6 + column_7 + column_8 + column_9
   list_of_columns = [string_of_columns[i:i+interval] for i in range(0, len(string_of_columns), interval)]
   return list_of_columns

def get_reverse_columns(puzzle_string):
   reverse_string = puzzle_string[::-1]
   interval = 10
   column_1 = reverse_string[::10]
   column_2 = reverse_string[1::10]
   column_3 = reverse_string[2::10]
   column_4 = reverse_string[3::10]
   column_5 = reverse_string[4::10]
   column_6 = reverse_string[5::10]
   column_7 = reverse_string[6::10]
   column_8 = reverse_string[7::10]
   column_9 = reverse_string[8::10]
   column_10 = reverse_string[9::10]
   string_of_columns = column_1 + column_2 + column_3 + column_4 + column_5 + column_6 + column_7 + column_8 + column_9
   reverse_list_of_columns = [string_of_columns[i:i+interval] for i in range(0, len(string_of_columns), interval)]
   return reverse_list_of_columns

def single_word_finder_row(list_of_rows, word):
   if word in ''.join(list_of_rows):
      index = ''.join(list_of_rows).index(word)
      column = index%10
      row = index//10
      return [True, column, row]
   return [False]

def single_word_finder_column(list_of_columns, word):
   if word in ''.join(list_of_columns):
      index = ''.join(list_of_columns).index(word)
      column = index//10
      row = index%10
      return [True, column, row]
   return [False]

def single_word_finder_reverse_row(reverse_list_of_rows, word):
   if word in ''.join(reverse_list_of_rows):
      normal_list_of_rows = ''.join(reverse_list_of_rows[10::-1][::-1]) 
      index = normal_list_of_rows.index(word)
      column = 9 - index%10
      row = 9 - index//10
      return [True, column, row]
   return [False]

def single_word_finder_reverse_column(reverse_list_of_columns, word):
   if word in ''.join(reverse_list_of_columns):
      normal_list_of_columns = ''.join(reverse_list_of_columns[10::-1][::-1])
      index = normal_list_of_columns.index(word)
      column = 9 - index//10
      row = 9 - index%10
      return [True, column, row]
   return [False]

def multiple_word_finder(puzzle_string, words):
   list_of_words = words.split(" ", words.count(" "))
   index = 0
   list_of_columns = get_columns(puzzle_string)
   list_of_rows = get_rows(puzzle_string)
   reverse_list_of_rows = get_reverse_rows(puzzle_string)
   reverse_list_of_columns = get_reverse_columns(puzzle_string)
   while index < len(list_of_words):
      word = list_of_words[index]
      row_finder = single_word_finder_row(list_of_rows, word)
      column_finder = single_word_finder_column(list_of_columns, word)
      reverse_row_finder = single_word_finder_reverse_row(reverse_list_of_rows, word)
      reverse_column_finder = single_word_finder_reverse_column(reverse_list_of_columns, word)
      if row_finder[0] == True:
         print("{:s}: (FORWARD) row: {:d} column: {:d}".format(word, row_finder[2], row_finder[1]))
         index += 1
         continue
      if column_finder[0] == True:
         print("{:s}: (DOWN) row: {:d} column: {:d}".format(word, column_finder[2], column_finder[1])) 
         index += 1
         continue
      if reverse_row_finder[0] == True:
         print("{:s}: (BACKWARD) row: {:d} column: {:d}".format(word, reverse_row_finder[2], reverse_row_finder[1])) 
         index += 1
         continue
      if reverse_column_finder[0] == True:
         print("{:s}: (UP) row: {:d} column: {:d}".format(word, reverse_column_finder[2], reverse_column_finder[1]))
         index += 1
         continue
      else: 
         print("{:s}: word not found".format(word))
         index += 1
