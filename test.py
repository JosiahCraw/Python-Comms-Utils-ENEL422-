from comms_utils import encode, decode

if __name__ == "__main__":
    pam_levels = 8
    encoded_data = encode.encode_pam_file("file.txt", pam_levels)
    print(encoded_data)
    print('Sent Data Length: {}'.format(len(encoded_data)))
    data = decode.decode_pam(encoded_data, pam_levels)
    print(data)
