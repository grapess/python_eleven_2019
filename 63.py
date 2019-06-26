def line(symbol,times) :
	result = ""
	count = 1
	while count <= times:
		result += symbol
		count += 1
	print(result)

line(symbol='-',times=20)
print(" Hello ")
line(times=30,symbol='=')
print(" Grapess ")
line('~',40)
print(" Solutions ")
line('_',50)