from utilities import text_block

def vigenere(text, keyword, decrypt=False, letters='abcdefghijklmnopqrstuvwxyz'):
    """
    Encrypts or decrypts a text using the Vigenere cipher.

    This is the one that uses the Tabula Recta.
    """

    newtext = ""
    text = text.lower()
    keyword = keyword.lower()
    keyword_len = len(keyword)
    if decrypt:
        for i, l in enumerate(text):
            newtext += letters[(letters.index(l) - letters.index(keyword[i % keyword_len])) % 26]
    else:
        for i, l in enumerate(text):
            newtext += letters[(letters.index(l) + letters.index(keyword[i % keyword_len])) % 26]

    if decrypt:
        return newtext
    else:
        return text_block(newtext.upper())