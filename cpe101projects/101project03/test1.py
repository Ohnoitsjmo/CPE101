def get_cages():
   index = 1
   number_of_cages = int(input("Number of cages: "))
   list_of_entries = list('')
   while index <= number_of_cages:
      cage_number = input(("Cage number {:d}: ".format(index - 1))).split()
      cage_number = [int(a) for a in cage_number]
      list_of_entries.append(cage_number)
      index += 1
   print(list_of_entries)
get_cages()
