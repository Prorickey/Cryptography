from ciphers import vigenere


def autokey(plaintext, primer, decrypt=False, letters='abcdefghijklmnopqrstuvwxyz'):
    """
    Encrypts or decrypts a text using the autokey cipher.
    """

    primer = primer.lower()
    plaintext = plaintext.lower()

    if decrypt is False:
        return vigenere(plaintext, primer + plaintext, letters=letters)
    
    ciphertext = plaintext.replace(" ", "")
    plaintext = ""
    key = primer 
    for i, l in enumerate(ciphertext):
        pl = letters[(letters.find(l) - letters.find(key[i])) % 26]
        key += pl 
        plaintext += pl 

    return plaintext.lower()