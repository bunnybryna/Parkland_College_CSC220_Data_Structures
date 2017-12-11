#!/usr/local/bin/python3.5

# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
from avl_tree import AVLTreeMap


print ("Content-type: text/html\n\n")

#filename = sys.argv[1]  # command line arg
filename = "theRoadNotTaken.txt"
#freq = {}
#freq = UnsortedTableMap()
#freq = SortedTableMap()
freq = AVLTreeMap()

for piece in open(filename).read().lower().split():
  # only consider alphabetic characters within this piece
  word = ''.join(c for c in piece if c.isalpha())
  if word:                                # require at least one alphabetic character
    freq[word] = 1 + freq.get(word, 0)

max_word = ''
max_count = 0
for (w,c) in freq.items():    # (key, value) tuples represent (word, count)
  if c > max_count:
    max_word = w
    max_count = c
print('The most frequent word is', max_word)
print('Its number of occurrences is', max_count)

print ("""
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" xml:space="preserve" style="shape-rendering:geometricPrecision; text-rendering:geometricPrecision; image-rendering:optimizeQuality; fill-rule:evenodd; clip-rule:evenodd"
viewBox="0 0 2000 1000">
    <circle style="fill:url(#toning);stroke:#010101;stroke-width:1.6871;stroke-miterlimit:10;" cx="1000" cy="20" r="19">
    </circle>
    <text x="1000" y="20" text-anchor="middle" >Root</text>

    <circle style="fill:url(#toning);stroke:#010101;stroke-width:1.6871;stroke-miterlimit:10;" cx="500" cy="40" r="19">
    </circle>
    <text x="500" y="40" text-anchor="middle" >Left</text>
</svg>
""")

# how to get information out of a node
for node in freq.breadthfirst():
  print ( "Node depth:" + str(freq.depth(node)) )
  print ( "Node height:" + str(freq.height(node)) )
  print ( "Node value:" + str(node.value()) )
  print ( "Node key:" + str(node.key()) )
  print ( "<br/>")
