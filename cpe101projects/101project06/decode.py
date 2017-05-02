# Project 6 - Images
#
# Name: Justin Mo
# Instructor: Brian Jones
# Section: 17

import sys
def groups_of_3(values):
   return [values[index:index + 3] for index in range(0, len(values), 3)]

try:
   my_file = open(sys.argv[1], "r")
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
   txt_file = open("decoded.ppm", "w")
   txt_file.write(line_1)
   txt_file.write(line_2)
   txt_file.write(line_3)
   for group in grouped:
      red = group[0] 
      green = group[1]
      blue = group[2]
      if int(red)*10 <= 255:
         red = int(red) * 10
         blue = red
         green = blue
         txt_file.write("{:d}\n".format(int(red)))
         txt_file.write("{:d}\n".format(int(green)))
         txt_file.write("{:d}\n".format(int(blue)))
      else:
         red = 255
         green = 255
         blue = 255
         txt_file.write("{:d}\n".format(int(red)))
         txt_file.write("{:d}\n".format(int(green)))
         txt_file.write("{:d}\n".format(int(blue)))
   txt_file.close()
except IndexError:
   print("Usage: python3 decode.py <image>")
   sys.exit(1)
except FileNotFoundError:
   print("Unable to open {:s}".format(sys.argv[1]))
   sys.exit(1)
except PermissionError:
   print("Unable to open {:s}".format(sys.argv[1]))
   sys.exit(1)

