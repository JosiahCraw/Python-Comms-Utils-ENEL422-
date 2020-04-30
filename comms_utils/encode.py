import numpy as np

def encode_pam(data: str, levels: int):
    levels = np.log2(levels)
    levels = int(levels)
    binary_data = ''.join(format(ord(char), 'b').zfill(8) for char in data)
    encoded_data = [int(binary_data[i:i+levels], 2) for i in range(0, len(binary_data), levels)]
    return encoded_data[::-1]

def encode_pam_file(file_name: str, levels: int):
    with open(file_name, 'r') as report:
        message = report.read()
        signal = encode_pam(message, levels)
    return signal

if __name__ == "__main__":
    print(encode_pam("This is a test ", 4))