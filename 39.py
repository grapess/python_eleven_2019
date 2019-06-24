count = 1

result = ""
while count <= 100 :
	if count == 50 :
		break
	count += 1
	if count % 2 == 0 :
		continue
	result += " [ " + str(count) + " ]"
	
	
print( result )