if n % 2 != 0:
    print('Weird')
else:
	if n >= 2 and n <= 5:
		print('Not Weird')
	elif n >= 6 and n <= 20:
		print('Weird')
	else:
		print('Not Weird')

if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a + b)
print(a - b)
print(a * b)

# // integer division, / float division
print (a // b)
print (a / b)

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
		if year % 100 != 0 or year % 400 == 0:
			leap = True
    
    return leap
	
for i in range(n):
	print i