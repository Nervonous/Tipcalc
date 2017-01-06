def tip(x, y):
		
	try: 
		x = int(x) 
		y = int(y)
		
	
	except ValueError:
		print "Must be integures"

	tip = x * 100 / y
	gt = 20 * y / 100
	correct = False
	

	while correct == False:

		
		print "Currently you're tiping %d percent" % tip
		print "A 20 percent tip would be %d." % gt
		print "Would you like to change your tip?"

		answer = raw_input("> ")
		
		if answer == "yes":
			
			cx = False
	
			while cx == False:
				print "What would you like your new tip to be?"
	
				x = raw_input("> ")


				try:
					x = int(x)
					cx = True
		

				except ValueError:
					print "Must be integures"


			nt = x * 100 / y

		
	
			if nt < tip and gt:
				print "Oh dear, must not have been good service."
				print "Very well your new tip is %d and percent is %d" % (x, nt)
				
				correct = True
				
	
			elif nt > tip and gt:
				print "Wow how generous of you!"
				print "Your new tip is %d and percent %d" % (x, nt)

				correct = True

			elif nt < tip and np >= gt:
				print "Still very generous!"
				print "Your new tip is %d and percent %d" % (x, nt)
			
				correct = True

			elif nt > tip and np < gt:
				print "Well still a better tip!"
				print "Your new tip is %d and percent %d" % (x, nt)

				correct = True
				

			
					
		elif answer == "no":

			print "Very well your tip is still %d or %d percent" % (x, tip)

			correct = True

				
		else:
	
			print "Please answer with 'yes' or 'no'."





	


	