def calculate_byte_checksum():
    data_byte1 = 0b11001100
    data_byte2 = 0b10101010
    checksum_result = data_byte1 ^ data_byte2
    print(f"Target result: {checksum_result}")

calculate_byte_checksum()