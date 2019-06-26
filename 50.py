'''
1
22
333
4444
55555
'''

row = 1
while row <= 5:
	result = ""
	
	col = 1
	while col <= row:
		result += str(row)
		col += 1
		
	print( result )
	row += 1