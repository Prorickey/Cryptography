from utilities import chi_squared, mod_inverse
from ciphers import affine, multiplicative, caesar


def brute_force_affine(cipher):
	"""
	Brute forces an affine cipher encoded text and returns the keys
	:param cipher: Affine encoded ciphertext
	:return: (km, ka, score) keys used to **encode** the text and the chi score of the decoded text
	"""

	scores = []
	for km in range(26):
		if mod_inverse(km, 26) == None:
			continue
		for ka in range(26):
			msg = multiplicative(caesar(cipher, ka, True), km, True)
			score = 50 #chi_squared(msg)

			print(f"CHI-SCORE({km}, {ka}): {score} - {msg}")

			scores.append((km, ka, score))

			if score < 1:
				return km, ka, score

	km, ka, score = min(scores, key=lambda x: x[2])
	return km, ka, score