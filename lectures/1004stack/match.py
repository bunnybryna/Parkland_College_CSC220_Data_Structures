#!/usr/local/bin/python3.5
import cgi,cgitb
cgitb.enable()

from stack import ArrayStack

def is_matched(expr):
	lefty = '({['
	righty = ')}]'
	S = ArrayStack()
	for c in expr:
		if c in lefty:
			S.push(c)
		elif c in righty:
			if S.is_empty():
				return False
			if righty.index(c)!=lefty.index(S.pop()):
				return False
	return S.is_empty()

print ('Content-Type: text/html\n');

formInfo = cgi.FieldStorage()

exp = formInfo.getvalue("exp")

if is_matched(exp):
	print(exp + ' is a matched set')
else:
	print(exp + ' is not a matched set')	
	
