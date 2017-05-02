def max_101(x,y):
   if x > y:
      return int(x)
   else:
      return int(y)


def max_of_three(x,y,z):
   if x>y and x>z:
      return float(x)
   elif y>x and y>z:
      return float(y)
   else:
      return float(z)


def rental_late_fee(days):
   if days <= 0:
      return 0
   if days <= 9:
      return 5
   if days <= 15:
      return 7
   if days <= 24:
      return 19
   if days > 24:
      return 100


def main():
   print(max_101(2,3))
   print(max_of_three(2,3,4))
   print(rental_late_fee(9))
