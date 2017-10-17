def play(lst, index, answer):
	# base case	
	if index == len(lst)-1:
		return answer
	# add the first step
	if index == 0:
		answer.append(index)	
	step = lst[index]
	next = index + step	
	# cell not visited and 0 not in the cell 	
	if next not in answer and step != 0:
		# first right then left
		if next < len(lst):
			answer.append(next)
			return play(lst, next, answer)
		else:
			next = index - step
			if next not in answer and next > 0:
				answer.append(next)
				return play(lst, next, answer)
			else:
				return []
	else:
		return []

# test case 1: 0 in the cell
#print(play([1,0,1],0,[]))
# test case 2: 0 in the last cell
#print(play([1,1,2,1,0],0,[]))
# test case 3: keep going right
#print(play([1,2,1,2,3,4,3,1,1,1],0,[]))
# test case 4: right then left
#print(play([1,2,2,2,3,3,1,1],0,[]))
