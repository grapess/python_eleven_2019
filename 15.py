n1 = int( input(" Enter First  Number : "))

n2 = int( input(" Enter Second Number : "))

n3 = int( input(" Enter Third  Number : "))

result = ""

if n1 == n2 :
	if n1 == n3 :
		result = " All Three Number are Equal "
	else:
		if n1 > n3 :
			result = " First and Second Number are Largest "
		else :
			result = " Third Number is Largest "
else:
	if n1 == n3 :
		if n1 > n2 :
			result = " First and Third Number are Largest "
		else :
			result = "Second Number is Largest "
	else :
		if n2 == n3 :
			if n2 > n1 :
				result = " Second and Third Number are Largest "
			else :
				result = " First Number is Largest "
		else:
			if n1 > n2 :
				if n1 > n3 :
					result = " First Number is Largest "
				else :
					result = " Third Number is Largest "
			else :
				if n2 > n3 :
					result = " Second Number is Largest "
				else :
					result = " Third Number is Largest "
print( result ) 