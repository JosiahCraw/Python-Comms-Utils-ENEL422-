import numpy as np

def encode_pam(data: str, levels: int):
    levels = np.log2(levels)
    levels = int(levels)
    binary_data = ''.join(format(ord(char), 'b').zfill(8) for char in data)
    i = len(binary_data)
    encoded_data = list()
    while(i > 0):
        binary_set = binary_data[i-levels:i]
        encoded_data.append(int(binary_set,2))
        i -= levels
    return encoded_data

if __name__ == "__main__":
    print(encode_pam("This is a test ", 4))