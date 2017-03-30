my_file = open("in.txt", "r")
line_number = 1
for line in my_file:
   print("Line {:d} ({:d} chars): {:s}".format(line_number, len(line.rstrip()), line.rstrip()))
   line_number += 1
my_file.close()
