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
	

wordsUnsorted = ['I', 'Love', 'You']	
wordsSorted, numCompare, numSwap= bubbleSort(wordsUnsorted)

print(wordsSorted)
print(numCompare)
print(numSwap)