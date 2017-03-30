 # Project 1
 #
 # Name: Justin Mo
 # Instructor: Brian Jones
 # Section: 17

import math

def  pounds_to_kg(pounds):
   return pounds*0.453592


def get_mass_object(obj):
   if obj == "t":
      return 0.1
   if obj == "p":
      return 1.0
   if obj == "r":
      return 3.0
   if obj == "g":
      return 5.3
   if obj == "l":
      return 9.07
   else:
      return 0.0


def get_velocity_object(distance):
   return math.sqrt((9.8*distance)/2)

def get_velocity_skater(mass_skater, mass_object, velocity_object):
   return (mass_object*velocity_object)/(mass_skater)


