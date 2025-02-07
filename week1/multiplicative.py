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
        num = (n * key) % 26

        cipher += list(alphabet)[num]

    return cipher

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def multiplicative_decode(text, key):
    return multiplicative_encode(text, mod_inverse(key, 26))


print(multiplicative_decode("jmafvlahhmu", 3))
print(multiplicative_decode("OZCGWUNDEQCPW", 7))