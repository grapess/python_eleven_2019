num = int( input(" Enter Any Number : "))
print(" Prime Factor of Given Number ")

result = ""
temp = num 
div = 2
while div <= temp :
	if temp % div == 0 :
		result += " [ " + str(div) + " ]"
		temp = temp // div
	else:
		div = div + 1
		
print( result )