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
elif rem == 1 :
	result += "Tuesday"
elif rem == 2 :
	result += "Wednesday"
elif rem == 3 :
	result += "Thursday"
elif rem == 4 :
	result += "Friday"
elif rem == 5 :
	result += "Saturday"
else :
	result += "Sunday"

result += "."

print( result )