def number_to_word( div ):
	one_to_ninteen = ("","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Forteen","Fifteen","Sixteen","Seventeen","Eighteen","Ninteen")
	twenty_to_ninty = ("","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninty")
	result = " "
	if div < 20 :
		result += one_to_ninteen[div]
	else :
		d1 = div // 10
		d2 = div % 10
		if d1 != 0:
			result += twenty_to_ninty[d1]
		if d2 != 0:
			if d1 != 0:
				result += " "
			result += one_to_ninteen[d2]
	return result


num = int( input(" Enter Any Number : "))

temp = num 
result = ""

if temp == 0:
	result += " Zero"
else:
	if temp < 0 :
		temp = temp * -1
		result += " -ve"
	div = temp // 10000000
	if div != 0 :
		result += number_to_word(div) + " Crore"
		
	temp = temp % 10000000
	div = temp // 100000
	if div != 0 :
		result += number_to_word( div ) + " Lac"
		
	temp = temp % 100000
	div = temp // 1000
	if div != 0 :
		result += number_to_word( div ) + " Thousand"
		
	temp = temp % 1000
	div = temp // 100
	if div != 0 :
		result += number_to_word( div ) + " Hundred"
		
	div = temp % 100
	if div != 0 :
		result += number_to_word(div)

result += "."
	
print( result )