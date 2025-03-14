from utilities import text_block


def vigenere(text, keyword, decrypt=False, letters='abcdefghijklmnopqrstuvwxyz'):
    """
    Encrypts or decrypts a text using the Vigenere cipher.

    This is the one that uses the Tabula Recta.
    """

    newtext = ""
    text = text.lower().replace(" ", "")
    keyword = keyword.lower()
    keyword_len = len(keyword)
    for i, l in enumerate(text):
        keyword_index = letters.find(keyword[i % keyword_len])
        if decrypt:
            keyword_index = -keyword_index

        newtext += letters[(letters.find(l) + keyword_index) % 26]

    if decrypt:
        return newtext
    else:
        return text_block(newtext.upper())

