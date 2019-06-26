'''
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
'''

space = 4
star = 1
row = 1
while row <= 9:
	result = ""
	
	col = 1
	while col <= space:
		result += " "
		col += 1
	
	col = 1
	while col <= star:
		if col == 1 or col == star :
			result += "*"
		else :
			result += " "
		col += 1
		
	print( result )
	if row < 5:
		star += 2
		space -= 1
	else:
		star -= 2
		space += 1
	row += 1