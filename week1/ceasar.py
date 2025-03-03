from ..utilities import text_block


def caesar_encode(text, key, decrypt=False, LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    cipher = ""
    if decrypt:
        key = 26 - key
    for l in text:
        if LETTERS.find(l.upper()) == -1:
            continue

        num = (LETTERS.index(l.upper()) + key) % 26

        cipher += LETTERS[num]

    if decrypt:
        return cipher.lower()
    else:
        return text_block(cipher.upper())


def ceasar_decode(text, key):
    return caesar_encode(text, 26-key)


# text = "thismessagewillsufficeformypurpose"
# res = []
# for i in range(1000):
#     r = ceasar_encode(text, i)
#     if r not in res:
#         res.append(r)
#
# print(len(res))

print(ceasar_decode("KPZJBZZPVUMVYBT", 7))
print(ceasar_decode("LZWQUGEWTQKWS", 18))