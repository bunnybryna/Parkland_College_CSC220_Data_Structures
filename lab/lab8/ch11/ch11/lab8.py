# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 10:46:05 2017

@author: bryna
"""

from avl_tree import AVLTreeMap

import cgi, cgitb
cgitb.enable()

print ("Content-type: text/html\n\n")

freq = AVLTreeMap()

formInfo = cgi.FieldStorage()
#paragraph = formInfo.getvalue("paragraph")
paragraph = "this is bryna bryna bryna\r\nbryna bryna"
if paragraph == None:
  print('')
else:
  lines = paragraph.lower().split('\r\n')
  for line in lines:
    # only consider alphabetic characters
    for word in line.split():
        if word:                                
            freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0
for (w,c) in freq.items():    # (key, value) tuples represent (word, count)
  if c > max_count:
    max_word = w
    max_count = c
print('The most frequent word is', max_word)
print('Its number of occurrences is', max_count)
