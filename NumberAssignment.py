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
		result += " "
		if div < 20 :
			if div == 1 :
				result += "One"
			elif div == 2 :
				result += "Two"
			elif div == 3 :
				result += "Three"
			elif div == 4 :
				result += "Four"
			elif div == 5 :
				result += "Five"
			elif div == 6 :
				result += "Six"
			elif div == 7 :
				result += "Seven"
			elif div == 8 :
				result += "Eight"
			elif div == 9 :
				result += "Nine"
			elif div == 10 :
				result += "Ten"
			elif div == 11 :
				result += "Eleven"
			elif div == 12 :
				result += "Twelve"
			elif div == 13 :
				result += "Thirteen"
			elif div == 14 :
				result += "Forteen"
			elif div == 15 :
				result += "Fifteen"
			elif div == 16 :
				result += "Sixteen"
			elif div == 17 :
				result += "Seventeen"
			elif div == 18 :
				result += "Eighteen"
			elif div == 19 :
				result += "Ninteen"
		else :
			d1 = div // 10
			d2 = div % 10
			if d1 != 0:
				if d1 == 2 :
					result += "Twenty"
				elif d1 == 3 :
					result += "Thirty"
				elif d1 == 4 :
					result += "Forty"
				elif d1 == 5 :
					result += "Fifty"
				elif d1 == 6 :
					result += "Sixty"
				elif d1 == 7 :
					result += "Seventy"
				elif d1 == 8 :
					result += "Eighty"
				elif d1 == 9 :
					result += "Ninty"
			if d2 != 0:
				if d1 != 0:
					result += " "
				if d2 == 1 :
					result += "One"
				elif d2 == 2 :
					result += "Two"
				elif d2 == 3 :
					result += "Three"
				elif d2 == 4 :
					result += "Four"
				elif d2 == 5 :
					result += "Five"
				elif d2 == 6 :
					result += "Six"
				elif d2 == 7 :
					result += "Seven"
				elif d2 == 8 :
					result += "Eight"
				elif d2 == 9 :
					result += "Nine"
		result += " Crore"
		
	temp = temp % 10000000
	div = temp // 100000
	if div != 0 :
		result += " "
		if div < 20 :
			if div == 1 :
				result += "One"
			elif div == 2 :
				result += "Two"
			elif div == 3 :
				result += "Three"
			elif div == 4 :
				result += "Four"
			elif div == 5 :
				result += "Five"
			elif div == 6 :
				result += "Six"
			elif div == 7 :
				result += "Seven"
			elif div == 8 :
				result += "Eight"
			elif div == 9 :
				result += "Nine"
			elif div == 10 :
				result += "Ten"
			elif div == 11 :
				result += "Eleven"
			elif div == 12 :
				result += "Twelve"
			elif div == 13 :
				result += "Thirteen"
			elif div == 14 :
				result += "Forteen"
			elif div == 15 :
				result += "Fifteen"
			elif div == 16 :
				result += "Sixteen"
			elif div == 17 :
				result += "Seventeen"
			elif div == 18 :
				result += "Eighteen"
			elif div == 19 :
				result += "Ninteen"
		else :
			d1 = div // 10
			d2 = div % 10
			if d1 != 0:
				if d1 == 2 :
					result += "Twenty"
				elif d1 == 3 :
					result += "Thirty"
				elif d1 == 4 :
					result += "Forty"
				elif d1 == 5 :
					result += "Fifty"
				elif d1 == 6 :
					result += "Sixty"
				elif d1 == 7 :
					result += "Seventy"
				elif d1 == 8 :
					result += "Eighty"
				elif d1 == 9 :
					result += "Ninty"
			if d2 != 0:
				if d1 != 0:
					result += " "
				if d2 == 1 :
					result += "One"
				elif d2 == 2 :
					result += "Two"
				elif d2 == 3 :
					result += "Three"
				elif d2 == 4 :
					result += "Four"
				elif d2 == 5 :
					result += "Five"
				elif d2 == 6 :
					result += "Six"
				elif d2 == 7 :
					result += "Seven"
				elif d2 == 8 :
					result += "Eight"
				elif d2 == 9 :
					result += "Nine"
		result += " Lac"
		
	temp = temp % 100000
	div = temp // 1000
	if div != 0 :
		result += " "
		if div < 20 :
			if div == 1 :
				result += "One"
			elif div == 2 :
				result += "Two"
			elif div == 3 :
				result += "Three"
			elif div == 4 :
				result += "Four"
			elif div == 5 :
				result += "Five"
			elif div == 6 :
				result += "Six"
			elif div == 7 :
				result += "Seven"
			elif div == 8 :
				result += "Eight"
			elif div == 9 :
				result += "Nine"
			elif div == 10 :
				result += "Ten"
			elif div == 11 :
				result += "Eleven"
			elif div == 12 :
				result += "Twelve"
			elif div == 13 :
				result += "Thirteen"
			elif div == 14 :
				result += "Forteen"
			elif div == 15 :
				result += "Fifteen"
			elif div == 16 :
				result += "Sixteen"
			elif div == 17 :
				result += "Seventeen"
			elif div == 18 :
				result += "Eighteen"
			elif div == 19 :
				result += "Ninteen"
		else :
			d1 = div // 10
			d2 = div % 10
			if d1 != 0:
				if d1 == 2 :
					result += "Twenty"
				elif d1 == 3 :
					result += "Thirty"
				elif d1 == 4 :
					result += "Forty"
				elif d1 == 5 :
					result += "Fifty"
				elif d1 == 6 :
					result += "Sixty"
				elif d1 == 7 :
					result += "Seventy"
				elif d1 == 8 :
					result += "Eighty"
				elif d1 == 9 :
					result += "Ninty"
			if d2 != 0:
				if d1 != 0:
					result += " "
				if d2 == 1 :
					result += "One"
				elif d2 == 2 :
					result += "Two"
				elif d2 == 3 :
					result += "Three"
				elif d2 == 4 :
					result += "Four"
				elif d2 == 5 :
					result += "Five"
				elif d2 == 6 :
					result += "Six"
				elif d2 == 7 :
					result += "Seven"
				elif d2 == 8 :
					result += "Eight"
				elif d2 == 9 :
					result += "Nine"
		result += " Thousand"
		
	temp = temp % 1000
	div = temp // 100
	if div != 0 :
		result += " "
		if div < 20 :
			if div == 1 :
				result += "One"
			elif div == 2 :
				result += "Two"
			elif div == 3 :
				result += "Three"
			elif div == 4 :
				result += "Four"
			elif div == 5 :
				result += "Five"
			elif div == 6 :
				result += "Six"
			elif div == 7 :
				result += "Seven"
			elif div == 8 :
				result += "Eight"
			elif div == 9 :
				result += "Nine"
			elif div == 10 :
				result += "Ten"
			elif div == 11 :
				result += "Eleven"
			elif div == 12 :
				result += "Twelve"
			elif div == 13 :
				result += "Thirteen"
			elif div == 14 :
				result += "Forteen"
			elif div == 15 :
				result += "Fifteen"
			elif div == 16 :
				result += "Sixteen"
			elif div == 17 :
				result += "Seventeen"
			elif div == 18 :
				result += "Eighteen"
			elif div == 19 :
				result += "Ninteen"
		else :
			d1 = div // 10
			d2 = div % 10
			if d1 != 0:
				if d1 == 2 :
					result += "Twenty"
				elif d1 == 3 :
					result += "Thirty"
				elif d1 == 4 :
					result += "Forty"
				elif d1 == 5 :
					result += "Fifty"
				elif d1 == 6 :
					result += "Sixty"
				elif d1 == 7 :
					result += "Seventy"
				elif d1 == 8 :
					result += "Eighty"
				elif d1 == 9 :
					result += "Ninty"
			if d2 != 0:
				if d1 != 0:
					result += " "
				if d2 == 1 :
					result += "One"
				elif d2 == 2 :
					result += "Two"
				elif d2 == 3 :
					result += "Three"
				elif d2 == 4 :
					result += "Four"
				elif d2 == 5 :
					result += "Five"
				elif d2 == 6 :
					result += "Six"
				elif d2 == 7 :
					result += "Seven"
				elif d2 == 8 :
					result += "Eight"
				elif d2 == 9 :
					result += "Nine"
		result += " Hundred"
		
	div = temp % 100
	if div != 0 :
		result += " "
		if div < 20 :
			if div == 1 :
				result += "One"
			elif div == 2 :
				result += "Two"
			elif div == 3 :
				result += "Three"
			elif div == 4 :
				result += "Four"
			elif div == 5 :
				result += "Five"
			elif div == 6 :
				result += "Six"
			elif div == 7 :
				result += "Seven"
			elif div == 8 :
				result += "Eight"
			elif div == 9 :
				result += "Nine"
			elif div == 10 :
				result += "Ten"
			elif div == 11 :
				result += "Eleven"
			elif div == 12 :
				result += "Twelve"
			elif div == 13 :
				result += "Thirteen"
			elif div == 14 :
				result += "Forteen"
			elif div == 15 :
				result += "Fifteen"
			elif div == 16 :
				result += "Sixteen"
			elif div == 17 :
				result += "Seventeen"
			elif div == 18 :
				result += "Eighteen"
			elif div == 19 :
				result += "Ninteen"
		else :
			d1 = div // 10
			d2 = div % 10
			if d1 != 0:
				if d1 == 2 :
					result += "Twenty"
				elif d1 == 3 :
					result += "Thirty"
				elif d1 == 4 :
					result += "Forty"
				elif d1 == 5 :
					result += "Fifty"
				elif d1 == 6 :
					result += "Sixty"
				elif d1 == 7 :
					result += "Seventy"
				elif d1 == 8 :
					result += "Eighty"
				elif d1 == 9 :
					result += "Ninty"
			if d2 != 0:
				if d1 != 0:
					result += " "
				if d2 == 1 :
					result += "One"
				elif d2 == 2 :
					result += "Two"
				elif d2 == 3 :
					result += "Three"
				elif d2 == 4 :
					result += "Four"
				elif d2 == 5 :
					result += "Five"
				elif d2 == 6 :
					result += "Six"
				elif d2 == 7 :
					result += "Seven"
				elif d2 == 8 :
					result += "Eight"
				elif d2 == 9 :
					result += "Nine"

result += "."
	
print( result )