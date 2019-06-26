'''
    1
   121
  12321
 1234321
123454321
'''

row = 1
while row <= 5:
	result = ""
	
	col = 1
	while col <= 5 - row:
		result += " "
		col += 1
	
	col = 1
	while col <= row:
		result += str(col)
		col += 1
		
	col = row - 1
	while col >= 1:
		result += str(col)
		col -= 1
		
	print( result )
	row += 1