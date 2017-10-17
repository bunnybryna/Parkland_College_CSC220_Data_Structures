#!/usr/local/bin/python3.5

from stack import ArrayStack

theStack = ArrayStack()

theList = [1,2,4,6,8,9,12,14,16]

for item in theList:
	theStack.push(item)

while not theStack.is_empty():
	print(theStack.pop())
