mapping = {}

plaintext = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ciphertext = "RSTUVWXYZMICHAELBDFGJKNOPQ"

for p, c in zip(plaintext, ciphertext):
    mapping[p] = c

def encrypt(text, mapping):
    encrypted_text = ""
    for char in text.upper():
        if char in mapping:
            encrypted_text += mapping[char]
        else:
            encrypted_text += char
    return encrypted_text

text = "Me and my roomate are on the gym grind. We make 1500 calorie dinners every other night :)"
encrypted_text = encrypt(text, mapping)

print(encrypted_text)