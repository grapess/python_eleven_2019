year = int( input(" Enter Any Year : " ))

# Normal year :- 365 days = 52 Weeks + 1 Day
# Leap Year :- 366 days = 52 Weeks + 2 Day

totaldays = ( year - 1 ) * 365
totaldays += ( year - 1 ) // 4
totaldays -= ( year - 1 ) // 100
totaldays += ( year - 1 ) // 400

rem = totaldays % 7

result = " On 1st January, " + str(year) + " has "

if rem == 0 :
	result += "Monday"
else:
	if rem == 1 :
		result += "Tuesday"
	else:
		if rem == 2 :
			result += "Wednesday"
		else :
			if rem == 3 :
				result += "Thursday"
			else:
				if rem == 4 :
					result += "Friday"
				else:
					if rem == 5 :
						result += "Saturday"
					else :
						result += "Sunday"

result += "."

print( result )