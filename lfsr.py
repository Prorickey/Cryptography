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