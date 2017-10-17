class Color:
	def __init__(self, red=0, green=0, blue=0):
		self._red, self._green, self._blue = red, green, blue
	
	def get_red(self):
		return self._red

	def get_green(self):
		return self._green

	def get_blue(self):
		return self._blue

	def set_colors(self, red, green, blue):
		self._red = red
		self._green = green
		self._blue = blue
		
	def __str__(self):
		return 'rgb(' + str(self._red) + ',' + str(self._green) + ',' + str(self._blue) + ')'

	#<circle fill="rgb(205,133,63)"/>	
	def SVG(self):
		return '<circle fill='+'"rgb(' + str(self._red) + ',' + str(self._green) + ',' + str(self._blue) + ')"/>'
		
# c1 = Color()
# print c1
# print c1.SVG()
# c2 = Color(255,255,255)
# print(c2.get_red())
# print(c2.get_green())
# print(c2.get_blue())
# c2.set_colors(66, 134, 244)
# print c2.SVG()		