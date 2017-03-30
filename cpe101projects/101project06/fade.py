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
   radius = sys.argv[4]
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
   txt_file = open("faded.ppm", "w")
   txt_file.write(line_1)
   txt_file.write(line_2)
   txt_file.write(line_3)
   list_of_two = line_2.split()
   line_number = 0
   x1 = int(sys.argv[3])
   y1 = int(sys.argv[4])
   for group in grouped:
      x2 = int(line_number)//int(list_of_two[1])
      y2 = int(line_number)%int(list_of_two[0])
      distance = math.sqrt((x1 - x2)**2 + (y1- y2)**2)
      red = group[0] 
      green = group[1]
      blue = group[2]
      if int(red)*((int(radius)-int(distance))/(int(radius))) <= 255:
         red = int(red)*((int(radius)-int(distance))/(int(radius)))
         txt_file.write("{:d}\n".format(abs(int(red))))
      if int(green)*((int(radius)-int(distance))/(int(radius))) <= 255:
         green = int(green)*((int(radius)-int(distance))/(int(radius)))
         txt_file.write("{:d}\n".format(abs(int(green))))
      if int(blue)*((int(radius)-int(distance))/(int(radius))) <= 255:
         blue = int(blue)*((int(radius)-int(distance))/(int(radius)))
         txt_file.write("{:d}\n".format(abs(int(blue))))
      if int(red)*((int(radius)-int(distance))/(int(radius))) > 255:
         red = 255
         txt_file.write("{:d}\n".format(abs(int(red))))
      if int(green)*((int(radius)-int(distance))/(int(radius))) > 255:
         green = 255
         txt_file.write("{:d}\n".format(abs(int(green))))
      if int(blue)*((int(radius)-int(distance))/(int(radius))) > 255:         
         blue = 255
         txt_file.write("{:d}\n".format(abs(int(blue))))
      line_number += 1
   txt_file.close()
except IndexError:
   print("Usage: python3 fade.py <image> <row> <column> <radius>")
   sys.exit(1)
except FileNotFoundError:
   print("Unable to open {:s}".format(sys.argv[1]))
   sys.exit(1)
except PermissionError:
   print("Unable to open {:s}".format(sys.argv[1]))
   sys.exit(1)

