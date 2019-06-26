def line(symbol='-',times=40) :
	result = ""
	count = 1
	while count <= times:
		result += symbol
		count += 1
	print(result)

line()
print(" Hello ")
line('*')
print(" Grapess ")
line(times=60)
print(" Solutions ")
line('_',50)