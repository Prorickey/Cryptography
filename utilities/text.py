def text_clean(text, LETTERS='ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
	ret = ""
	LETTERS += LETTERS.upper()
	LETTERS += LETTERS.lower()
	for l in text:
		if LETTERS.find(l) != -1:
			ret += l

	return ret.upper()


def text_block_old(t, n=5):
	f = ""
	i = 0
	for l in t:
		if i % n == 0 and i != 0:
			f += " "

		f += l
		i += 1

	return f