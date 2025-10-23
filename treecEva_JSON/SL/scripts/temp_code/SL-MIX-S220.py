def tokenize_and_transform(payload):
    tokens = [ord(c) for c in payload]
    transformed = []
    for i, val in enumerate(tokens):
        if i % 3 == 0:
            transformed.append(val << 2)
        elif i % 3 == 1:
            transformed.append(val >> 1)
        else:
            transformed.append(val ^ 0xFF)
    return transformed

def compute_checksum(matrix):
    xor_accum = 0
    for row in matrix:
        row_sum = sum(row)
        xor_accum ^= row_sum
    return xor_accum

payload = "SECURITY2023"
token_stream = tokenize_and_transform(payload)
grid_size = 4
matrix_form = [token_stream[i:i+grid_size] for i in range(0, len(token_stream), grid_size)]
checksum_val = compute_checksum(matrix_form)
key_modifier = (lambda x: x & 0xF0)(sum(token_stream) ^ 0xAA)
transmission_code = checksum_val | key_modifier
print(f"Result: {transmission_code}")