import utility
from utility import *

class Point:
   """Attributes: x and y"""
   def __init__(self, x, y):
      self.x = x
      self.y = y
   
   def __eq__(self, other):
      return epsilon_equal(self.x, other.x) and epsilon_equal(self.y, other.y)

class Circle:
   """Attributes: Point and Radius"""
   def __init__(self, x, y, radius=0):
      self.x = x
      self.y = y
      self.radius = radius
   
