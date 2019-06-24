num = int( input(" Enter Any Number : "))

isprime = True

count = 0
if num % 2 == 0 or num % 3 == 0:
	isprime = False
	count = 1
else :
	div = 5	
	count = 1
	while div * div <= num :
		count += 1
		if num % div == 0 or num % ( div + 2 ) == 0:
			isprime = False
			break
		div += 6

if isprime :
	print(" Given Number is Prime ")
else :
	print(" Given Number is Composite ")
	
print(" Total Count : " , count )