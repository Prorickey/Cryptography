def mod_inverse(a, m):
	for i in range(1, m):
		if (a * i) % m == 1:
			return i
	return None


def multiplicative_encode(text, key, letters="abcdefghijklmnopqrstuvwxyz"):
	cipher = ""
	for l in text.lower():
		if letters.find(l) == -1:
			continue
		print(letters.find(l))
		num = (letters.find(l) * key) % len(letters)

		cipher += letters[num]

	return cipher


def multiplicative_decode(text, key, letters="abcdefghijklmnopqrstuvwxyz"):
	return multiplicative_encode(text, mod_inverse(key, len(letters)), letters)

