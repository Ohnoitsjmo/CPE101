import driver

def letter(row, col):
   if (row >= 2 and row <= 4 and col >= 3 and col <= 6):
      return 'M' 
   else: 
      return 'S'
if __name__ == '__main__':
   driver.compare_patterns(letter)
