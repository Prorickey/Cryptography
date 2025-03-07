def substitution_encode(text, sub, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    encrypted_text = ""
    for char in text.upper():
        encrypted_text += sub[letters.find(char)]
    return encrypted_text


def substitution_decode(text, sub, letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    decrypted_text = ""
    for char in text.upper():
        decrypted_text += letters[sub.find(char)]
    return decrypted_text