# Project 6 - Images
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17

import sys
import math
def groups_of_3(values):
   return [values[index:index + 3] for index in range(0, len(values), 3)]

try:
   my_file = open(sys.argv[1], "r")
except IndexError:
   print("Usage: python3 blur.py <image> [<reach>]")
   sys.exit(1)
except FileNotFoundError:
   print("Unable to open {:s}".format(sys.argv[1]))
   sys.exit(1)
except PermissionError:
   print("Unable to open {:s}".format(sys.argv[1]))
   sys.exit(1)
res = []
for line in my_file:
   res.append(line.rstrip())
grouped = groups_of_3(res[3:])
file_name = open(sys.argv[1])
lines = file_name.readlines()
line_1 = lines[0]
line_2 = lines[1]
line_3 = lines[2]
file_name.close()
txt_file = open("blurred.ppm", "w")
txt_file.write(line_1)
txt_file.write(line_2)
txt_file.write(line_3)
list_of_two = line_2.split()
try:
   reach = int(sys.argv[2])
except: 
   reach = 4
new_grouped = [grouped[x:x+int(list_of_two[0])] for x in range(0, len(grouped),int(list_of_two[0]))]
index = 0
for every_list in new_grouped:
   for every_small in every_list:
      index += 1
new_index = 0
final_index = 0
count = ((2*reach + 1) **2)
for new_index in range(0, index):
#(for every pixel)
   try:
      matrix = []
      for list_index in range(2*reach + 1):   
         matrix.append(grouped[new_index:new_index+(2*reach + 1)])
      red_val = 0
      blue_val = 0
      green_val = 0
      for each_row in matrix:
         for pixel in each_row:
            red_val += int(pixel[0])
            blue_val += int(pixel[1])
            green_val += int(pixel[2])
      txt_file.write("{:d}\n".format(int(abs(red_val/count))))
      txt_file.write("{:d}\n".format(int(abs(blue_val/count))))
      txt_file.write("{:d}\n".format(int(abs(green_val/count))))
   except ZeroDivisionError:
      sys.exit(1)
   except IndexError:
      sys.exit(1)
txt_file.close()

