from functools import reduce
from itertools import combinations

def transform_layer(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return ''.join(chr((ord(c) + 3) % 128) for c in result)
    return wrapper

class NucleotideProcessor:
    def __init__(self):
        self.codon_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    
    @transform_layer
    def process_sequence(self, sequence):
        complement = ''.join(self.codon_map.get(n, n) for n in sequence)
        reversed_complement = complement[::-1]
        return reversed_complement

def count_valid_codons(transformed_seq):
    valid_codons = ['ATG', 'TAA', 'TAG', 'TGA']
    codon_count = 0
    for i in range(0, len(transformed_seq)-2):
        if transformed_seq[i:i+3] in valid_codons:
            codon_count += 1
    return codon_count

# Main processing pipeline
processor = NucleotideProcessor()
original_sequences = ['ATGCCGTAG', 'TTGACCTGA', 'CGTACGTAA']
transformed_sequences = []

for seq in original_sequences:
    transformed = processor.process_sequence(seq)
    transformed_sequences.append(transformed)

# Apply filtering based on length
filtered_sequences = list(filter(lambda s: len(s) > 6, transformed_sequences))

# Generate all possible pairwise combinations
sequence_pairs = list(combinations(filtered_sequences, 2))

# Concatenate pairs and count codons
codon_counts = []
for pair in sequence_pairs:
    concatenated = pair[0] + pair[1]
    count = count_valid_codons(concatenated)
    codon_counts.append(count)

# Calculate final metric
final_codon_count = reduce(lambda x, y: x + (y * 2 if y > 0 else 1), codon_counts, 0)
print(f'Result: {final_codon_count}')