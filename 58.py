print(" Armstrong Number between 1 and 500 ")

result = ""
num = 1

while num <= 500 :
	d1 = num // 100
	d2 = ( num // 10 ) % 10
	d3 = num % 10
	sum = d1 ** 3 + d2 ** 3 + d3 ** 3
	if num == sum :
		result += " [ " + str(num) + " ]"
	num += 1
	
print( result )