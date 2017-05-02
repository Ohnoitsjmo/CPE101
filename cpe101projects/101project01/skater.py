 # Project 1
 #
 # Name: Justin Mo
 # Instructor: Brian Jones
 # Section: 17

import funcs
import math

def main():
   kg = funcs.pounds_to_kg(float(input("How much do you weigh (pounds)? ")))
  
   meters = int(input("How far away is your professor (meters)? "))

   object_velocity = funcs.get_velocity_object(float(meters))
  
   object = funcs.get_mass_object(str(input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ightsaber, or lawn (g)nome? ")))       

   print()

   velocity = funcs.get_velocity_skater(kg,object,object_velocity)

   if object <= 0.1:
      print("Nice throw! You're going to get an F!")

   if object > 0.1 and object <= 1.0:
      print("Nice throw! Make sure your professor is OK.")

   if object > 1.0 and  meters >= 20:
      print("Nice throw! RIP professor.")

   if object > 1.0 and  meters < 20:
      print("Nice throw! How far away is the hospital?")

   print("Velocity of skater: {:.3f} m/s" .format(velocity))
  	
   if velocity < 0.2:
      print("My grandmother skates faster than you!")
     
   if velocity >= 0.2 and velocity < 1.0:    
      pass

   if velocity >= 1.0:
      print("Look out for that railing!!!")

if __name__ == "__main__":
   main()
