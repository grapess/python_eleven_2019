total = 21

while True :
	print(" Total Remaining Matchstick : " , total )
	
	print("\n User can pick 1 or 2 or 3 or 4 Matchstick ")
	pick = int( input(" Enter your Number of stick you want to Pick : "))
	
	if pick >= 1 and pick <= 4 :
		computer_pick = 5 - pick
		print("\n Computer Pick : ", computer_pick , " Matchstick ")
		total -= 5
	else:
		print("\n Invalid Number of Pick. So Try Again ")
		
	if total == 1 :
		break
		
print("\n There are remaining 1 Matchstick and User turn ")
print(" So Computer Wins ")