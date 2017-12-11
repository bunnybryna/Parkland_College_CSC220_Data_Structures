

#!/usr/local/bin/python3.5

import sys
from avl_tree import AVLTreeMap

import cgi, cgitb
cgitb.enable()

print ("Content-type: text/html\n\n")

freq = AVLTreeMap()

formInfo = cgi.FieldStorage()
#paragraph = formInfo.getvalue("paragraph")
paragraph = "yes this is bryna bryna hey, yes, this is Bryna yeah"
#paragraph = '''May indulgence difficulty ham can put especially. Bringing remember for supplied her why was confined. Middleton principle did she procuring extensive believing add. Weather adapted prepare oh is calling. 
#These wrong of he which there smile to my front. He fruit oh enjoy it of whose table. Cultivated occasional old her unpleasing unpleasant. At as do be against pasture covered viewing started. Enjoyed me settled mr respect no spirits civilly.  '''
if paragraph == None:
  print('')
else:
  lines = paragraph.lower().split('\r\n')
  for line in lines:
    # only consider alphabetic characters
    for word in line.split():
        if word.isalpha():                                
            freq[word] = 1 + freq.get(word, 0)
            
#for (w,c) in freq.items():
    #print (w,c)

print("""
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
xml:space="preserve" style="shape-rendering:geometricPrecision; 
text-rendering:geometricPrecision; image-rendering:optimizeQuality; 
fill-rule:evenodd; clip-rule:evenodd" viewBox="0 0 2000 1000">""")
string = ""
betweenSpace = 0
currentDepth = 0
for node in freq.breadthfirst():
    if freq.depth(node) > 6:
        break;
    else:
        if freq.depth(node) == 0 or freq.depth(node) != currentDepth:
            x = 2000/(2**(freq.depth(node)+1))
            betweenSpace = x * 2
            currentDepth = freq.depth(node)
        else:
            x = x + betweenSpace
        string += "<circle style='fill:url(#toning);stroke:#010101;stroke-width:1.6871;stroke-miterlimit:10;' cx='"
        string += str(x)
        string += "' cy='"
        y = str((freq.depth(node)+1)*20)
        string += y
        string += "' r='19'></circle><text x='"
        string += str(x)
        string += "'y='"
        string += y
        string +="' text-anchor='middle' >"
        string +=str(node.key())+" "+str(node.value())
        string +="</text>"
string +="</svg>"
print(string)
        

