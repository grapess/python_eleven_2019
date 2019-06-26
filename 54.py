'''
    1
   1 1
  1 3 1
 1 3 3 1
1 3 5 3 1
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
		if col % 2 == 0 :
			result += " "
		else :
			result += str(col)
		col += 1
		
	col = row - 1
	while col >= 1:
		if col % 2 == 0 :
			result += " "
		else :
			result += str(col)
		col -= 1
		
	print( result )
	row += 1