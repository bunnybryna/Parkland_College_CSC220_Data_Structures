#!/usr/local/bin/python3.5
# I honor Parkland's core values by affirming that I have
# followed all academic integrity guidelines for this work.
# Bryna Zhao

from chain_hash_map import ChainHashMap
        
import cgi, cgitb
cgitb.enable()

print("Content-Type: text/html\n");


#filename = 'mydict.txt'
filename = '/home/staff/kurban/public/lists/web2.txt'
# use hash map to store the dictionary
theDict = ChainHashMap()

for piece in open(filename).read().lower().split():
    word = ''.join(c for c in piece if c.isalpha())
    if word:
        theDict[word] = 1 + theDict.get(word, 0)
        
#for word in theDict:
    #print(word + " : " + str(theDict[word]))

formInfo = cgi.FieldStorage()

sentence = formInfo.getvalue("sentence")
    
#sentence = "This is Bryna Zhao"
myList = sentence.lower().split()

notInDict = list()

for word in myList:
    if word not in theDict:
        #print(word)
        notInDict.append(word)
        
print("These words are not in the Dictionary: ")
for word in notInDict:
	print(word)

