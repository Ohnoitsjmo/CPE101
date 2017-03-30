puzzle = [[0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

row = 0
column = 0
value = 0
while value < 100:
   puzzle[row][column] = value
   print(puzzle)
   value += 1
   row += 1
   column += 1

print(puzzle[0])
print(puzzle[1])
print(puzzle[2])
print(puzzle[3])
print(puzzle[4])

