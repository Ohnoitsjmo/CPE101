import driver

def letter(row, col):
   if row == col:
      return 'X'
   if (row + col == 6):
      return 'X'
   else:
      return 'O'

if __name__ == '__main__':
   driver.compare_patterns(letter)
