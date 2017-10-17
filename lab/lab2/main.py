#!/usr/local/bin/python3.5
import random
from point import Point
from color import Color
from circle import Circle

# print the http response header
print ('Content-Type: text/html\n');

print ('''<html><head>
<title>lab2 Circle Bryna Zhao</title>
</head><body>''')

print('<svg height="1000" width="1000">')
circle_list = []
for i in range(15):
	r1 = random.randint(1,800)
	r2 = random.randint(1,500)
	cr = random.randint(0,255)
	cg = random.randint(0,255)
	cb = random.randint(0,255)	
	newCircle = Circle(Point(r1,r2),i,Color(cr,cg,cb))
	print(newCircle.SVG())

print('</svg>')
print ('</body></html>') 


