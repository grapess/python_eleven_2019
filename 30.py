from math import sqrt

num = int( input(" Enter Any Number : "))

isprime = True

count = 0
div = 2
if num % div == 0 :
	isprime = False
	count = 1
else :
	div = 3
	range = sqrt( num )
	count = 1
	while div <= range :
		count += 1
		if num % div == 0 :
			isprime = False
			break
		div += 2

if isprime :
	print(" Given Number is Prime ")
else :
	print(" Given Number is Composite ")
	
print(" Total Count : " , count )