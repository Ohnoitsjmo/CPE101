from objects import *
import objects
import math

def distance(Point1, Point2):
   return math.sqrt(abs(Point2.x - Point1.x)**2 + abs(Point2.y - Point1.y)**2)  

def circles_overlap(my_circle_1, my_circle_2):
   return distance(my_circle_1.center, my_circle_2.center) < (my_circle_1.radius+ my_circle_2.radius)
