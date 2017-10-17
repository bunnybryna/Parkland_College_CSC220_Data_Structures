

from point import Point
from color import Color
# center is a Point object, cx, cy
# fill is a Color object

class Circle:
	def __init__(self, center, radius, fill):
		self._center, self._radius, self._fill = center, radius, fill
		
	def get_center(self):
		return self._center

	def get_radius(self):
		return self._radius

	def get_fill(self):
		return self._fill		
	
	def set_circle(self, center, radius, fill):
		self._center._across = center.across
		self._center._down = center.down		
		self._radius = radius
		self._fill._red = fill.red
		self._fill._green = fill.green
		self._fill._blue = fill.blue
		
	#  <circle cx="50" cy="50" r="40" stroke="black" stroke-width="3" fill="red" />	
	def SVG(self):
		return '<circle cx="'+str(self._center._across)+'" cy="'+str(self._center._down)+'" r="'+str(self._radius)+'" fill="'+str(self._fill)+'"/>'
		

# print("Here is new")
# p2 = Point(1,2)
# print p2

# c2 = Color(66, 134, 244)
# print c2.SVG()

# circle = Circle(p2,3,c2)
# print(circle.SVG())	