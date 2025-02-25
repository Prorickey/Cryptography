ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def ceasar_encode(text, key):
    pre_key_list = []
    for letter in list(text):
        pre_key_list.append(ALPHABET.find(letter.lower()))

    cipher = ""
    for n in pre_key_list:
        num = (n + key) % 26

        cipher += list(ALPHABET)[num]

    return cipher


def ceasar_decode(text, key):
    return ceasar_encode(text, 26-key)


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