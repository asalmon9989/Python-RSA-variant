import rsa_modules

#waxon
def master_encoder(fname):
	"""Uses rsa_modules to encode an uncoded message."""
	message_list = []
	coded_message_list = []

	message = input("Message: ")

	print("Encoding message ...")
	message_list = rsa_modules.char2num(message)

	coded_message_list = rsa_modules.encode_lst(message_list)

	rsa_modules.message_export(coded_message_list, fname)

#waxoff
def master_decoder(fname):
	"""Uses rsa_modules to decode an encoded message."""
	import rsa_modules
	message_list = []
	coded_message_list = []

	coded_message_str = input("Coded message: ")

	print("Decoding message ...")
	coded_message_list = rsa_modules.decode_str(coded_message_str)

	message_list = rsa_modules.decode_lst(coded_message_list)

	message = rsa_modules.num2char(message_list)

	with open(fname, 'w') as file_object:
		file_object.write(message)