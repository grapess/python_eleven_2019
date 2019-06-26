num = int( input(" Enter Any Number : "))

result = ""

value = 2
while value <= 2 * num :
	result += " [ " + str(value) + " ]"
	value += 2
	
print( result )