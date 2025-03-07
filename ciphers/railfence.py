def rail_fence_encode(text, n):
    rows = []
    for i in range(n):
        rows.append("")

    rn = 0
    desc = False
    for i in range(len(text)):
        rows[rn] += text[i]
        if desc:
            if rn > 0:
                rn -= 1
            else:
                desc = False
                rn += 1
        else:
            if rn + 1 < n:
                rn += 1
            else:
                desc = True
                rn -= 1

    ciphertext = ""
    for row in rows:
        ciphertext += row

    return ciphertext.upper()

def rail_fence_decode(ciphertext, n):
    rail_map = [['\n' for _ in range(len(ciphertext))] for _ in range(n)]

    rn = 0
    desc = False

    for i in range(len(ciphertext)):
        rail_map[rn][i] = '*'
        if desc:
            if rn > 0:
                rn -= 1
            else:
                desc = False
                rn += 1
        else:
            if rn + 1 < n:
                rn += 1
            else:
                desc = True
                rn -= 1

    index = 0
    for r in range(n):
        for c in range(len(ciphertext)):
            if rail_map[r][c] == '*' and index < len(ciphertext):
                rail_map[r][c] = ciphertext[index]
                index += 1

    plaintext = ""
    rn = 0
    desc = False

    for i in range(len(ciphertext)):
        plaintext += rail_map[rn][i]
        if desc:
            if rn > 0:
                rn -= 1
            else:
                desc = False
                rn += 1
        else:
            if rn + 1 < n:
                rn += 1
            else:
                desc = True
                rn -= 1

    return plaintext