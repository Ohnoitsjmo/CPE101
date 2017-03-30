class Point:
   """Attributes: x and y"""
   def __init__(self, x, y):
      self.x = x
      self.y = y

class Circle:
   """Attributes: Point and Radius"""
   def __init__(self, center, radius=0):
      self.radius = radius
      self.center = Point(center[0], center[1])

