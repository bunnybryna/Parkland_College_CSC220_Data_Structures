#http://www.geeksforgeeks.org/linked-list-set-1-introduction/
#http://www.geeksforgeeks.org/linked-list-set-2-inserting-a-node/
#http://www.geeksforgeeks.org/linked-list-set-3-deleting-node/

class _Node:
	_slots_ = '_element','_next'
	def __init__(self, element, next):
		self._element = element
		self._next = next
		
list1 = ['a','b','c']
# just copy the address, both points to the same collection of char
listShallow = list1
# copy the whole list, 
listDeep = deepcopy(list1)
list1[2] = 'replaces'
print(listShallow)
print(listDeep)
print(id(list1))
print(id(listShallow))
print(id(listDeep))