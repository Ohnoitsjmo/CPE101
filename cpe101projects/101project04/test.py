def get_reverse_columns(puzzle_string):
   puzzle_string =  "WAQHGTTWEECBMIVQQELSAZXWKWIIILLDWLFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU"
   reverse_string = puzzle_string[::-1]
   interval = 10
   column_1 = reverse_string[::10]
   column_2 = reverse_string[1::10]
   column_3 = reverse_string[2::10]
   column_4 = reverse_string[3::10]
   column_5 = reverse_string[4::10]
   column_6 = reverse_string[5::10]
   column_7 = reverse_string[6::10]
   column_8 = reverse_string[7::10]
   column_9 = reverse_string[8::10]
   column_10 = reverse_string[9::10]
   string_of_columns = column_1 + column_2 + column_3 + column_4 + column_5 + column_6 + column_7 + column_8 + column_9
   reverse_list_of_columns = [string_of_columns[i:i+interval] for i in range(0, len(string_of_columns), interval)]
   return reverse_list_of_columns
   
