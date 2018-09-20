while True:
		gross = input ("")
		kids = input ("")
		try:
			gross=int (gross)
		except:
			print ("invalid")
			continue
		try:
			int_kids = int (kids)
		except:
			print ("invalid")
			continue
		if gross<0 or kids<0 or kids>50:
			print ("invalid")
			continue
		if int_kids != float(kids):
			print("invalid")
			continue
		break

