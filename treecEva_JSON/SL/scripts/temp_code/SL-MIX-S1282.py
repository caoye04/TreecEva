from collections import defaultdict

def encode_dna(seq):
    mapping = {'A': '00', 'T': '01', 'G': '10', 'C': '11'}
    return ''.join(mapping[nuc] for nuc in seq)

def decode_dna(binary_str):
    reverse_mapping = {'00': 'A', '01': 'T', '10': 'G', '11': 'C'}
    nucleotides = []
    for i in range(0, len(binary_str), 2):
        nucleotides.append(reverse_mapping[binary_str[i:i+2]])
    return ''.join(nucleotides)

# Initial DNA sequence
initial_sequence = 'ATGC'

# Encode the sequence to binary
encoded_binary = encode_dna(initial_sequence)

# Convert binary string to integer for bitwise operations
binary_integer = int(encoded_binary, 2)

# Apply transformation: XOR with mask and right shift
mask = 0b10101010
transformed_value = (binary_integer ^ mask) >> 2

# Convert back to binary string, ensuring leading zeros are preserved
transformed_binary = bin(transformed_value)[2:].zfill(len(encoded_binary))

# Decode transformed binary back to nucleotide sequence
transformed_sequence = decode_dna(transformed_binary)

# Count occurrences of each nucleotide using defaultdict
nucleotide_counter = defaultdict(int)
for nucleotide in transformed_sequence:
    nucleotide_counter[nucleotide] += 1

# Short-circuit evaluation to determine final count
final_nucleotide_count = nucleotide_counter['G'] if 'G' in nucleotide_counter else 0 or \
                         sum(nucleotide_counter.values()) if nucleotide_counter else -1

print(f"Result: {final_nucleotide_count}")