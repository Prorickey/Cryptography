alphabet = "abcdefghijklmnopqrstuvwxyz"
l_map = {}
for i in range(len(alphabet)):
    l_map[alphabet[i]] = i


def ceasar_encode(text, key):
    pre_key_list = []
    for letter in list(text):
        pre_key_list.append(l_map[letter.lower()])

    cipher = ""
    for n in pre_key_list:
        num = (n + key) % 26

        cipher += list(alphabet)[num]

    return cipher

def ceasar_decode(text, key):
    return ceasar_encode(text, 26-key)


print(ceasar_decode("KPZJBZZPVUMVYBT", 7))
print(ceasar_encode("ilovetocode", 8))