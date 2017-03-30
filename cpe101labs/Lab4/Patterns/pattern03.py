import driver

def letter(row, col):
   if (row <= 19 and  col <=9):
      return 'X'
   else:
      return 'O'

if __name__ == '__main__':
   driver.compare_patterns(letter)
