import waxon_waxoff as wax
cycle = True

while cycle:
	"""Select desired operation"""
	action = input("(1) ENCODE MESSAGE\n(2) DECODE MESSAGE\n" + 
					"(3) ESCAPE\n... ")
	"""Determining appropriate response ..."""
	if action == '1':
		filename = input("Please specify output file path.\n")
		wax.master_encoder(filename)
		print("Done.\n")
	elif action == '2':
		filename = input("Please specify output file path.\n")
		wax.master_decoder(filename)
		print("Done.\n")
	elif action == '3':
		break
	else:
		print("INCORRECT INPUT VALUE\n")