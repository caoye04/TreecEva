from collections import Counter
from functools import reduce

def compute_positional_weight(char_freq_map, sequence_length):
    weighted_sum = 0
    for char, freq in char_freq_map.items():
        char_code = ord(char)
        position_factor = (char_code * freq) % 7
        weighted_sum += position_factor * (sequence_length // (freq + 1))
    return weighted_sum

def calculate_mutation_checksum(dna_sequence):
    # Step 1: Count nucleotide frequencies
    nucleotide_counter = Counter(dna_sequence)
    
    # Step 2: Apply positional weighting
    seq_len = len(dna_sequence)
    position_weight = compute_positional_weight(nucleotide_counter, seq_len)
    
    # Step 3: Transform sequence - reverse complement simulation
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    transformed_seq = ''.join(complement_map[nuc] for nuc in dna_sequence[::-1])
    
    # Step 4: Calculate transformation hash
    transform_hash = sum(ord(c) * (i+1) for i, c in enumerate(transformed_seq)) % 1000
    
    # Step 5: Combine metrics with modular arithmetic
    frequency_product = reduce(lambda x, y: (x * y) % 97, nucleotide_counter.values(), 1)
    
    # Step 6: Final checksum computation
    checksum_components = [
        position_weight % 13,
        transform_hash % 17,
        frequency_product % 19,
        seq_len % 23
    ]
    
    checksum_result = sum(component * (i + 11) for i, component in enumerate(checksum_components)) % 100
    return checksum_result

# Main execution
sample_dna = "ATCGATCGATCGATCGATCG"
checksum_result = calculate_mutation_checksum(sample_dna)
print(f"Result: {checksum_result}")