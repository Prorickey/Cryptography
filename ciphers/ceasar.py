from utilities import text_block

def caesar(text, key, decrypt=False, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    cipher = ""
    if decrypt:
        key = 26 - key
    for l in text:
        if letters.find(l.upper()) == -1:
            continue

        num = (letters.index(l.upper()) + key) % 26

        cipher += letters[num]

    if decrypt:
        return cipher.lower()
    else:
        return text_block(cipher.upper())
