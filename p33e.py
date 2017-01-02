# to continue, go to the while loops in the tip() function, that's where the problem is at the moment.




# ignore this function, this was something else i was playing with.
def test():
	p = int(raw_input("if> ")) * 100 / int(raw_input("of> "))
	
	while p < 80:
		print "still too low, only %d percent" % p
		
		p = int(raw_input("if> ")) * 100 / int(raw_input("of> "))

	if p > 80:
		print "Fantastic you achieved %d percent of our 80 percent goal!" % p



# I know this is extensive and there is a much simpler way to do it, but i wanted to play with concepts i learned.
def tip(x, y):
	"""Tip calculator"""
	t = x * 100 / y
	gt = y * 20 / 100
	if t < 20:
		print "You're tiping a bit low, you want about 20 percent but are tiping %d." % t
		print "A 20 percent tip for your bill is about %d, would you like to change your tip?" % gt
	
		answer = raw_input("> ")

		
		# here is the problem
		while answer != "yes" or "no":
				print "Please try again and answer with a 'yes' or 'no'"
				answer = raw_input("> ")
		

		if answer == "yes":
			print "Ok what would you like your new tip to be?"
			nt = int(raw_input("> "))
			
			if nt > gt:
				t = nt * 100 / y
				print "Very generous of you, your new tip percent is %d" % t
			
			elif t < nt < gt:
				t = nt * 100 / y
				print "Ah a slight increase still kind. Your new tip percent is %d" % t
			
			else:
				t = nt * 100 / y
				print "Oh dear, service must have been poor. Your new tip percent is %d" % t
		
		elif answer == "no":
			print "Very well your percent tipped is %d" % t


		
	elif t > 20:
		print "Your tip exceeds 20 percent, it's currently %d" % t
		print "In case this is a mistake would you like to change your tip?"

		
		# I know this one is not finished, wanted to fix the first one before finishing this one.
		answer = raw_input("> ")
		
		while answer != "yes" or "no":
			print "Please try again and answer with a 'yes' or 'no'"
		
		if answer == "yes":
			print "Ok, what would you like your new tip to be?"
			
			nt = int(raw_input("> "))
			
			if nt > t:
				t = nt * 100 / y
				print "My so generous! so %d is the new percent, bless you." % t

			elif 20 <= nt < t:
				t = nt * 100 / y
				print "%d is still very generous!" % t

			else:
				t = nt * 100 / y
				print "Ok, however keep in mind your new percent is %d, which is below 20" %d
	elif t == 20:
		print "Perfect 20 percent tip!" 
			
		
		