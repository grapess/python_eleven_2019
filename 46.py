'''
    *
   * *
  * * *
 * * * *
* * * * *
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
		if col % 2 == 0 :
			result += " "
		else :
			result += "*"
		col += 1
		
	print( result )
	row += 1