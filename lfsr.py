def lfsr(bits: list, res: list) -> str:
    xor = bits[1] ^ bits[4]
    print(xor)
    next1 = [xor] + bits[:-1]
    res.append(bits[-1])
    print(bits)
    if len(res) == 12:
        res = [str(x) for x in res]
        return ''.join(res)
    else:
        return lfsr(next1, res)

print(lfsr([1, 1, 0, 1, 1, 0], []))