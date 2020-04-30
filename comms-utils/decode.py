import numpy as np
from .encode import encode_pam
from typing import List

def decode_pam(incoming_data: List[int], levels: int):
    levels = int(np.log2(levels))
    bit_str = ""
    for level_val in incoming_data[::-1]:
        bit_str = bit_str + bin(level_val)[2:].zfill(levels)
    message = ''.join(char for char in [chr(int(bit_str[i:i+8], 2)) for i in range(0, len(bit_str), 8)])
    return message


if __name__ == "__main__":
    test_list = encode_pam("get out now", 16)
    print(decode_pam(test_list, 16))