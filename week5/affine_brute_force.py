from week5 import chi_squared
from utilities import affine, mod_inverse


def brute_force_affine(cipher):
	"""
	Brute forces an affine cipher encoded text and returns the keys
	:param cipher: Affine encoded ciphertext
	:return: (km, ka) keys used to encode the text
	"""

	fkm = 0
	fka = 0
	found = False
	for km in range(26):
		for ka in range(26):
			score = chi_squared(affine(cipher, km, ka, True))
			#print(f"CHI-SCORE({km}, {ka}): {score}")

			if score < 1:
				found = True
				fkm = km
				fka = ka
				break

		if found:
			break

	return fkm, fka

