from objects import *
import objects
from list_comp_tests import *
import list_comp_tests
from math import *
import math

def distance_all(list_of_points):
   return [math.sqrt(abs(Point.x)**2 + abs(Point.y)**2) for Point in list_of_points]
   
def are_in_first_quadrant(list_of_points):
   return [Point for Point in list_of_points if Point.x > 0 and Point.y > 0]

