won_bet = True 
big_win = True
if won_bet and  big_win:
	print("You can now stop betting!")

	#Using the or operator
	won_bet = True
	big_win = False
	if won_bet or big_win:
		print("You can now stop betting!")
		 