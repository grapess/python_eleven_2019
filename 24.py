num = int( input(" Enter Any Number : "))

sum = 0
temp = num
if temp < 0 :
	temp = temp * -1
	
while temp > 0:
	rem = temp % 10
	sum += rem
	temp = temp // 10
	
print(" Sum of Digit of Given Number : " , sum)