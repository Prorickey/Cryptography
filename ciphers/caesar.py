from utilities import text_block

def caesar_old(text, key, decrypt=False, letters="abcdefghijklmnopqrstuvwxyz"):
    """
    Encrypts or decrypts a text using the Caesar cipher.
    """

    cipher = ""
    text = text.lower()

    if decrypt:
        key = 26 - key
    for l in text:
        if letters.find(l) == -1:
            continue

        num = (letters.index(l) + key) % 26

        cipher += letters[num]

    if decrypt:
        return cipher.lower()
    else:
        return text_block(cipher.upper())
