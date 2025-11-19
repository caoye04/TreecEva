import itertools

def encode_sequence(seq):
    mapping = {'A': '00', 'T': '01', 'G': '10', 'C': '11'}
    binary_str = ''.join(mapping[nuc] for nuc in seq)
    return int(binary_str, 2)

nucleotides = ['A', 'T', 'G', 'C']
valid_sequences = []

for seq in itertools.product(nucleotides, repeat=4):
    first_nuc, second_nuc, third_nuc, fourth_nuc = seq
    starts_with_purine = first_nuc in ['A', 'G']
    ends_with_pyrimidine = fourth_nuc in ['T', 'C']
    is_valid = starts_with_purine and ends_with_pyrimidine
    valid_sequences.append(seq) if is_valid else None

encoded_values = [encode_sequence(seq) for seq in valid_sequences]
total_encoded_sum = sum(encoded_values)

print(f"Result: {total_encoded_sum}")