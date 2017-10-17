#!/usr/local/bin/python3.5

def countRecursive(l):
	# l == []
	if len(l) == 0:
		return 0
	return 1+ countRecursive(l[1:])

def leastElement(l):
	if len(l) == 1:
		return l[0]
	leastOfRest = leastElement(l[1:])
	if l[0] < leastOfRest:
		return l[0]
	else:
		return leastOfRest
 
import cgi, cgitb
cgitb.enable()

#print the http response header
print("Content-Type: text/html\n");

formInfo = cgi.FieldStorage()

sentence = formInfo.getvalue("sentence")
print("You entered: " + sentence)

listOfWords = sentence.split()
print("<br />")
print(listOfWords)

print("<br />")
print("Number of items is ")
print(countRecursive(listOfWords))

print("<br />")
print("Lowest item is")
print(leastElement(listOfWords))


