from ciphers import multiplicative
from ciphers_pkg.caesar import caesar


def affine(text, km, ka, decrypt=False, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	"""
	Encrypts or decrypts a text using the affine cipher.
	"""
	
	if decrypt:
		return multiplicative(caesar(text, ka, True, letters), km, True, letters.lower()).lower()
	else:
		return caesar(multiplicative(text, km, False, letters.lower()), ka, False, letters).upper()