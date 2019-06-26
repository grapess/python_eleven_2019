def line(symbol,times) :
	result = ""
	count = 1
	while count <= times:
		result += symbol
		count += 1
	print(result)

line('-',20)
print(" Hello ")
line('=',30)
print(" Grapess ")
line('~',40)
print(" Solutions ")
line('_',50)