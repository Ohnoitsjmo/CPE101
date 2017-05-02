def is_even(value):
   return value %2 == 0
#true

  
def in_an_interval(value):
   return value >= 2 and value <9 or  value>47 and value<92 or value>12 and value<= 19 or value>101 and value<103
#false

def main():
   print(is_even(2))
   print(in_an_interval(104))

