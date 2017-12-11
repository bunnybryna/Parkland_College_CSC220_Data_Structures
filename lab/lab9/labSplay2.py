#!/usr/local/bin/python3.5

import sys
import random
from splay_tree import SplayTreeMap

import cgi, cgitb
cgitb.enable()

print ("Content-type: text/html\n\n")

stree = SplayTreeMap()

rnlist = []

# make sure each time the same serial of random number for 3 programs
random.seed(3)

for n in range(10):
    rn = random.randint(0,100)
    rnlist.append(rn)
    stree[rn] = rn

print("Insert 10 random integers to the Splay Tree:")    
print(rnlist)

if rnlist[-1] in stree:   
    print("Search for the last element: "+str(rnlist[-1]))
    
#for (w,c) in stree.items():
    #print (w,c)

print("""
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
xml:space="preserve" style="shape-rendering:geometricPrecision; 
text-rendering:geometricPrecision; image-rendering:optimizeQuality; 
fill-rule:evenodd; clip-rule:evenodd" viewBox="0 0 2000 1000">""")
string = ""
betweenSpace = 0
currentDepth = 0
for node in stree.breadthfirst():
    if stree.depth(node) > 6:
        break;
    else:
        if stree.depth(node) == 0 or stree.depth(node) != currentDepth:
            x = 2000/(2**(stree.depth(node)+1))
            betweenSpace = x * 2
            currentDepth = stree.depth(node)
        else:
            x = x + betweenSpace
        string += "<circle style='fill:url(#toning);stroke:#010101;stroke-width:1.6871;stroke-miterlimit:10;' cx='"
        string += str(x)
        string += "' cy='"
        y = str((stree.depth(node)+1)*150)
        string += y
        string += "' r='19'></circle><text x='"
        string += str(x)
        string += "'y='"
        string += y
        string +="' text-anchor='middle' >"
        string +=str(node.value())
        string +="</text>"
string +="</svg>"
print(string)
        
