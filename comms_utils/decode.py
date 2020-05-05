import numpy as np
from typing import List

def decode_pam(incoming_data: List[int], levels: int):
    levels = int(np.log2(levels))
    bit_str = ""
    for level_val in incoming_data[::-1]:
        bit_str = bit_str + bin(level_val)[2:].zfill(levels)
    message = ''.join(char for char in [chr(int(bit_str[i:i+7], 2)) for i in range(0, len(bit_str), 7)])
    return message

def decode_pam_file(incoming_data: List[int], file_name: str, levels: int):
    decoded_data = decode_pam(incoming_data, levels)
    with open(file_name, 'w+') as output:
        output.writelines(decoded_data)

if __name__ == "__main__":
    print(decode_pam([], 16))
