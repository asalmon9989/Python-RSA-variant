import lock_and_key as loki

def char2num(msg):
	"""Convert each character in the messageg to associated Unicode 
		decimal value."""
	msg_lst = []
	for letter in msg:
		msg_lst.append(ord(letter))
	return msg_lst

def encode_lst(msg_lst):
	"""Takes and encodes numerical value attributed to each character."""
	lpk = loki.crypt_keeper()
	"""Stores lock, power, and key."""
	cod_msg_lst = [lpk[0], lpk[2]]
	for num in msg_lst:
		cod_msg_lst.append((num**lpk[1])%lpk[0])
	return cod_msg_lst

def message_export(cod_msg_lst, fname):
	"""Exports new encoded string to file of choosing."""
	with open(fname, 'w') as file_object:
		for i in range(len(cod_msg_lst)):
			file_object.write(str(cod_msg_lst[i]) + '.')

def decode_lst(cod_msg_lst):
	"""Takes and decodes numerical value encoded for each character."""
	msg_lst = []
	for num in cod_msg_lst[2:]:
		msg_lst.append((num**cod_msg_lst[1])%cod_msg_lst[0])
	return msg_lst

def decode_str(msg_str):
	"""Takes in encoded string and separates each value in a list."""
	msg_lst = []
	holding_i = 0
	for i in range(len(msg_str)):
		if msg_str[i] == '.':
			msg_lst.append(int(msg_str[holding_i:i]))
			holding_i = i+1
	return msg_lst

def num2char(msg_lst):
	"""Converts Unicode decimal back to associated character."""
	msg = ''
	for num in msg_lst:
		msg += chr(num)
	return msg
