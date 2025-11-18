from functools import reduce

def hex_to_binary_matrix(hex_str):
    # Convert hex to integer, then to binary string without '0b' prefix
    bin_str = bin(int(hex_str, 16))[2:].zfill(8)
    # Create a 2x4 matrix from the binary string
    return [[int(bin_str[i*4 + j]) for j in range(4)] for i in range(2)]

def matrix_xor(m1, m2):
    # Element-wise XOR of two 2x4 matrices
    return [[m1[i][j] ^ m2[i][j] for j in range(4)] for i in range(2)]

def matrix_sum(matrix):
    # Sum all elements in the matrix
    return sum(sum(row) for row in matrix)

def process_token(token):
    base_matrix = hex_to_binary_matrix(token)
    # Apply bitwise shift: left shift each element by its column index
    shifted = [[base_matrix[i][j] << j for j in range(4)] for i in range(2)]
    # Apply mask with 0xF (15 in decimal) using bitwise AND
    masked = [[shifted[i][j] & 15 for j in range(4)] for i in range(2)]
    return masked

tokens = ['A3', '1F', 'C5', '7B']
matrices = list(map(process_token, tokens))

# Aggregate matrices using XOR
aggregated = reduce(matrix_xor, matrices)

# Calculate checksum as sum of all elements multiplied by token count
checksum = matrix_sum(aggregated) * len(tokens)

print(f"Result: {checksum}")