n1 = int( input(" Enter First  Number : "))

n2 = int( input(" Enter Second Number : "))

n3 = int( input(" Enter Third  Number : "))

result = ""

if n1 == n2 and n1 == n3 :
	result = " All Three Number are Equal "
elif n1 == n2 and n1 > n3 :
	result = " First and Second Number are Largest "
elif n1 == n3 and n1 > n2 :
	result = " First and Third Number are Largest "
elif n2 == n3 and n2 > n1 :
	result = " Second and Third Number are Largest "
elif n1 > n2 and n1 > n3 :
	result = " First Number is Largest "
elif n2 > n3 :
	result = " Second Number is Largest "
else :
	result = " Third Number is Largest "
	
print( result ) 