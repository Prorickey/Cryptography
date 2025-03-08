from utilities import text_block

def substitution(text, sub, decrypt=False, letters="abcdefghijklmnopqrstuvwxyz"):
    """
    Encrypts or decrypts a text using the substitution cipher.
    """
    
    text = text.lower()
    newtext = ""
    if decrypt:
        for char in text.upper():
            newtext += letters[sub.find(char)]
    else:
        for char in text.upper():
            newtext += sub[letters.find(char)]

    if decrypt:
        return newtext
    else:
        return text_block(newtext.upper())