def compute_data_checksum(input_data):
    data_chars = list(input_data)
    temp_list = [ord(c) + 10 for c in data_chars]
    checksum_value = sum(ord(c) ^ idx for idx, c in enumerate(data_chars))
    length_check = len(data_chars)
    return checksum_value

input_string = "CODE42"
result = compute_data_checksum(input_string)
print(f"Result: {result}")