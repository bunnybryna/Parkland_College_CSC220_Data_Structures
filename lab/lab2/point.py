class Point:
	def __init__(self, across=0, down=0):
		self._across, self._down = across, down
	
	def get_across(self):
		return self._across
		
	def get_down(self):
		return self._down

	def set_cooridates(self, across, down):
		self._across = across
		self._down = down
		
	def __str__(self):
		return '<' + str(self._across) + ',' + str(self._down) + '>'
		
# p1 = Point()
# print p1
# print(p1.get_across())
# print(p1.get_down())

# p2 = Point(1,2)
# print p2
# p2.set_cooridates(2,4)
# print p2

