from ..utilities import mod_inverse

alphabet = "abcdefghijklmnopqrstuvwxyz"
l_map = {}
for i in range(len(alphabet)):
    l_map[alphabet[i]] = i


def multiplicative_encode(text, key):
    pre_key_list = []
    for letter in list(text):
        pre_key_list.append(l_map[letter.lower()])

    cipher = ""
    for n in pre_key_list:
        num = (n * key) % len(alphabet)

        cipher += list(alphabet)[num]

    return cipher


def multiplicative_decode(text, key):
    return multiplicative_encode(text, mod_inverse(key, len(alphabet)))


cipher = multiplicative_encode("hellothismessageisciphered", 343)
print(cipher)
print(multiplicative_decode(cipher, 343))
