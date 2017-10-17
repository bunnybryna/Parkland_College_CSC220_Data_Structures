#!/usr/local/bin/python3.5

def bubbleSort(l):
	n = len(l)
	compare = 0
	swap = 0
	# for i in range(n):
	for i in range(0,n-1):
		# for j in range(0,n-i-1):
		for j in range(0, n-1):
			compare += 1
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]
				swap += 1		
	return (l, compare, swap)		
 
import cgi, cgitb
cgitb.enable()

#print the http response header
print("Content-Type: text/html\n");

formInfo = cgi.FieldStorage()

sentence = formInfo.getvalue("sentence")
print("You entered: " + sentence)

wordsUnsorted = sentence.split()
print("<br />")
print("Unsorted: ")
print(wordsUnsorted)

wordsSorted, numCompare, numSwap= bubbleSort(wordsUnsorted)

print("<br />")
print("Sorted: ")
print(wordsSorted)

print("<br />")
print("compare happened " + str(numCompare) + " times")

print("<br />")
print("swap happened " + str(numSwap) + " times")


