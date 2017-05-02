import driver

def letter(row, col):
   if (row <= 9 and col <= 19):
      return 'R'
   else:
      return 'Q'
   

if __name__ == '__main__':
   driver.compare_patterns(letter)
