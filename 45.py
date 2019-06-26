'''
    *
   ***
  *****
 *******
*********
'''

row = 1
while row <= 5:
	result = ""
	
	col = 1
	while col <= 5 - row:
		result += " "
		col += 1
	
	col = 1
	while col <= 2 * row - 1:
		result += "*"
		col += 1
		
	print( result )
	row += 1