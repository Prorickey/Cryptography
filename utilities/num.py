def mod_inverse(a, m):
	for i in range(1, m):
		if (a * i) % m == 1:
			return i
	return None