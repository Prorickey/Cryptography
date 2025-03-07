from ciphers import caesar, multiplicative_decode, multiplicative_encode

def affine(text, km, ka, decrypt=False, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	if decrypt:
		return multiplicative_decode(caesar(text, ka, True, letters), km, letters.lower()).lower()
	else:
		return caesar(multiplicative_encode(text, km, letters.lower()), ka, False, letters).upper()