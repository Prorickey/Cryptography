from utilities import mod_inverse, text_block

def multiplicative(text, key, decrypt=False, letters="abcdefghijklmnopqrstuvwxyz"):
	"""
	Encrypts or decrypts a text using the multiplicative cipher.
	"""

	text = text.lower()
	newtext = ""
	if decrypt:
		key = mod_inverse(key, len(letters))

	for l in text.lower():
		if letters.find(l) == -1:
			continue
		num = (letters.find(l) * key) % len(letters)

		cipher += letters[num]

	if decrypt:
		return newtext
	else:
		return text_block(newtext.upper())