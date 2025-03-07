from utilities import mod_inverse


def multiplicative_encode(text, key, letters="abcdefghijklmnopqrstuvwxyz"):
	cipher = ""
	for l in text.lower():
		if letters.find(l) == -1:
			continue
		num = (letters.find(l) * key) % len(letters)

		cipher += letters[num]

	return cipher


def multiplicative_decode(text, key, letters="abcdefghijklmnopqrstuvwxyz"):
	return multiplicative_encode(text, mod_inverse(key, len(letters)), letters)