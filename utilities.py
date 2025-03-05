from week1.ceasar import caesar_encode, ceasar_decode
from week1.multiplicative import multiplicative_decode, multiplicative_encode


def text_clean(text, LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
	ret = ""
	LETTERS += LETTERS.upper()
	LETTERS += LETTERS.lower()
	for l in text:
		if LETTERS.find(l) != -1:
			ret += l

	return ret.upper()


def text_block(t, n=5):
	f = ""
	i = 0
	for l in t:
		if i % n == 0 and i != 0:
			f += " "

		f += l
		i += 1

	return f



def gcd(a, b):
	while b:
		a, b = b, a % b
	return a


def mod_inverse(a, m):
	for i in range(1, m):
		if (a * i) % m == 1:
			return i
	return None

def affine(text, km, ka, decrypt=False, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
	if decrypt:
		return ceasar_decode(multiplicative_decode(text, km), ka)
	else:
		return caesar_encode(multiplicative_encode(text, km), ka)