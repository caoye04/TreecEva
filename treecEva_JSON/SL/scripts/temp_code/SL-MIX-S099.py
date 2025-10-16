from collections import defaultdict
import math

def nucleotide_hash(dna_seq):
    mapping = {'A': 0, 'T': 1, 'G': 2, 'C': 3}
    hash_value = 0
    for nucleotide in dna_seq:
        hash_value = hash_value * 4 + mapping[nucleotide]
    return hash_value

def transform_marker(value):
    # Apply bitwise operations and mathematical transformations
    step1 = value & 0xFF  # Mask to 8 bits
    step2 = step1 ^ (step1 >> 2)  # XOR with right-shifted version
    step3 = (step2 * 17) % 256  # Multiply and modulo
    step4 = int(math.sqrt(step3)) if step3 >= 0 else 0  # Square root
    return step4

def calculate_gc_content(dna_seq):
    gc_count = sum(1 for nuc in dna_seq if nuc in 'GC')
    return gc_count / len(dna_seq) if dna_seq else 0

def process_genetic_marker(dna_sequence):
    # Hash the DNA sequence
    marker_hash = nucleotide_hash(dna_sequence)
    
    # Transform the hash value
    transformed_value = transform_marker(marker_hash)
    
    # Calculate GC content
    gc_ratio = calculate_gc_content(dna_sequence)
    
    # Combine metrics with weighted formula
    final_metric = int(transformed_value * (1 + gc_ratio) * 100)
    return final_metric

# Main processing
sequence = "ATGCGTACGT"
genetic_marker_map = defaultdict(int)
genetic_marker_map[sequence] = process_genetic_marker(sequence)

# Additional transformations
values = [genetic_marker_map[seq] for seq in [sequence]]
processed_values = [v for v in values if v > 0]

if processed_values:
    final_metric = sum(processed_values) // len(processed_values)
else:
    final_metric = 0
    
print(f"Result: {final_metric}")