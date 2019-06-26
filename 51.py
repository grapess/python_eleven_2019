'''
1
12
123
1234
12345
'''

row = 1
while row <= 5:
	result = ""
	
	col = 1
	while col <= row:
		result += str(col)
		col += 1
		
	print( result )
	row += 1