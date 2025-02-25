import random

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def mod_inverse(a, m):
	for i in range(1, m):
		if (a * i) % m == 1:
			return i
	return None

def affine_encrypt(text, a, b):
	if gcd(a, 26) != 1:
		raise ValueError("Key 'a' must be coprime with 26.")

	encrypted_text = ''
	for char in text:
		if char.isalpha():
			base = ord('A') if char.isupper() else ord('a')
			encrypted_text += chr(((a * (ord(char) - base) + b) % 26) + base)
		else:
			encrypted_text += char
	return encrypted_text

def affine_decrypt(ciphertext, a, b):
	if gcd(a, 26) != 1:
		raise ValueError("Key 'a' must be coprime with 26.")

	a_inv = mod_inverse(a, 26)
	if a_inv is None:
		raise ValueError("Modular inverse of 'a' does not exist.")

	decrypted_text = ''
	for char in ciphertext:
		if char.isalpha():
			base = ord('A') if char.isupper() else ord('a')
			decrypted_text += chr(((a_inv * ((ord(char) - base - b)) % 26) + base))
		else:
			decrypted_text += char
	return decrypted_text

# Example Usage
a, b = 5, 6  # Keys (a must be coprime with 26)
plaintext = "mathisfun"
ciphertext = affine_encrypt(plaintext, a, b)
decrypted_text = affine_decrypt("OAAXGXLCSXYD", a, b)

print("Encrypted:", ciphertext)
print("Decrypted:", decrypted_text)
