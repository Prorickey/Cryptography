from ..utilities import gcd, mod_inverse, text_block


def affine_encrypt(text, km, ka, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	cipher = ""
	for l in text:
		if letters.find(l.upper()) == -1:
			continue

		num = (letters.index(l.upper()) * km + ka) % 26

		cipher += letters[num]

	return text_block(cipher.upper())

