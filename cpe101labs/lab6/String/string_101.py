import char
from char import *

def str_rot_13(string):
   final_string = [char_rot_13(string[index]) for index in range(len(string))]
   return "".join(final_string) 

def str_translate_101(string, char_1, char_2):
   index = 0
   new_string = ""
   while index < len(string):
      char = string[index]
      index += 1
      if char != char_1:
         new_string += "".join(char)
      else:
         char = char_2
         new_string += "".join(char)   
   return new_string

