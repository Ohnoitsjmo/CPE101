# CPE 101 Lab 4
# Name: Justin Mo

def main():
   table_size = get_table_size()
   while table_size != 0:
      first = get_first()
      increment= get_increment()
      show_table(table_size, first, increment)
      table_size = get_table_size()

# Obtain a valid table size from the user
def get_table_size():
   size = int(input("Enter number of rows in table (0 to end): "))

   while size < 0:
      print("Size must be non-negative.")
      size = int(input("Enter number of rows in table (0 to end): "))
      
   return size

# Obtain the first table entry from the user 
def get_first():
   first = int(input("Enter the value of the first number in the table: "))

   while first < 0:
      print("First number must be non-negative.")
      first = int(input("Enter the value of the first number in the table: "))
      
   return first

def get_increment():
   increment = int(input("Enter the increment between rows: "))
   
   while increment < 0:
     print("Increment must be non-negative.")
     increment = int(input("Enter the increment between rows: "))

   return increment

# Display the table of cubes
def show_table(size, first, increment):
   print("A cube table of size %d will appear here starting with %d" % (size, first))
   print("Number  Cube")
   counter = 0
   sum_of_cubes = 0
   while counter < size:
      number = first + increment
      counter += 1
      first += increment
      sum_of_cubes += (number-increment) ** 3
      print("{:<6d}  {:d}".format(number-increment, (number-increment)**3))     
   print("")
   print("The sum of cubes is: {:3d}".format(sum_of_cubes))   
   print("")
# Insert Loop Here
   

if __name__ == "__main__":
   main()
