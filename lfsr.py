import math

def textToBinary(text):
    binary = []
    for char in text:
        binary.append(format(ord(char), "08b"))

    return binary 

def binaryToText(text1):
    if type(text1) is str:
        temp = text1 
        text1 = [temp[i:i+8] for i in range(0, len(temp), 8)]

    text = []
    for bin in text1:
        text.append(chr(int(bin, 2)))

    return text

def encode(bin1, bin2):
    cipherbin = []
    for i in range(len(bin1)):
        int1 = int(bin1[i], 2)
        key = int(bin2[i], 2)

        cipher = int1 ^ key 
        cipherbin.append(format(cipher, "08b"))

    return cipherbin 

plaintext = "binary text"
key = "jdkm"
key = ''.join(key for _ in range(math.ceil(len(plaintext) / len(key))))
ptext = textToBinary(plaintext)
k = textToBinary(key)
ciphertext = encode(ptext, k)
converted = encode(ciphertext, k)
print("Binary Representations")
print("Plaintext:   ", ptext)
print("Key:         ", k)
print("Ciphertext:  ", ciphertext)
print("Converted:   ", converted)
print("\nString Representations")
print("Plaintext:   ", plaintext)
print("Key:         ", key)
print("Ciphertext:  ", binaryToText(ciphertext))
print("Converted:   ", ''.join(binaryToText(converted)))

input = "0010001001110000101110011101100111010010011000101100101000001101"
print(''.join(binaryToText(input)))

def get_bit(value, bit_index):
    return (value >> (bit_index-1)) & 1

def lfsr6(seed, num_bits):
    current_state = seed
    output_stream = 0
    
    for _ in range(num_bits-1):
        output_stream = (output_stream << 1) | get_bit(current_state, 1)
        xor = (get_bit(current_state, 1) ^ get_bit(current_state, 2)) ^ get_bit(current_state, 3)
        current_state = (current_state >> 1) | (xor << 5)
        
    return output_stream

keystream = lfsr6(0b011011, 64)

inp = 0b0010001001110000101110011101100111010010011000101100101000001101
print(bin(inp))
print(bin(keystream))
plaintext = inp ^ keystream
print(bin(plaintext))
print(binaryToText("0" + bin(plaintext)[2:]))

print(textToBinary("Name"))

def get_bit(value, bit_index):
    return (value >> (bit_index-1)) & 1

def lfsr8(seed, num_bits):
    """
            8 7 6 5 4 3 2 1 (bits == 8)
           ┌─┬─┬─┬─┬─┬─┬─┬─┐
        ┌─→│1│0│1│0│0│0│0│1├─→ output
        │  └─┴─┴─┴┬┴┬┴┬┴─┴┬┘
        └──────XOR┘ │ │   │
                └─XOR └─┐ │
                    └──XOR┘
                          (taps == 5, 4, 3, 1)
    """
    current_state = seed
    output_stream = 0
    
    for i in range(num_bits):
        output_stream = (output_stream << 1) | get_bit(current_state, 1)
        xor = (((get_bit(current_state, 1) ^ get_bit(current_state, 3)) ^ get_bit(current_state, 4)) ^ get_bit(current_state, 5))
        current_state = (current_state >> 1) | (xor << 7)
        
    return output_stream