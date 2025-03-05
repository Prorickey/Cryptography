from ..utilities import text_block
from ..week1 import caesar_encode, ceasar_decode, multiplicative_encode, multiplicative_decode

def affine_encrypt(text, km, ka, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	cipher = ""
	for l in text:
		if letters.find(l.upper()) == -1:
			continue

		num = (letters.index(l.upper()) * km + ka) % 26

		cipher += letters[num]

	return text_block(cipher.upper())

def affine(text, km, ka, decrypt=False, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	if decrypt:
		return ceasar_decode(multiplicative_decode(text, km), ka)
	else:
		return caesar_encode(multiplicative_encode(text, km), ka)