import re
from functools import wraps

def validate_dna_sequence(func):
    @wraps(func)
    def wrapper(seq):
        if not re.match(r'^[ACGT]+$', seq):
            raise ValueError("Invalid DNA sequence")
        return func(seq)
    return wrapper

@validate_dna_sequence
def process_genomic_data(dna_seq):
    # Step 1: Encode nucleotides to numerical values
    encoding_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    encoded_values = [encoding_map[nucleotide] for nucleotide in dna_seq]
    
    # Step 2: Apply bitwise operations for compression (greedy approach)
    compressed_segments = []
    i = 0
    while i < len(encoded_values):
        current_segment = encoded_values[i]
        count = 1
        while i + count < len(encoded_values) and encoded_values[i] == encoded_values[i + count]:
            count += 1
        compressed_segments.append((current_segment, count))
        i += count
    
    # Step 3: Sort segments by frequency (descending) then by value (ascending)
    sorted_segments = sorted(compressed_segments, key=lambda x: (-x[1], x[0]))
    
    # Step 4: Pattern matching to remove redundant segments
    unique_segments = []
    seen_values = set()
    for segment in sorted_segments:
        if segment[0] not in seen_values:
            unique_segments.append(segment)
            seen_values.add(segment[0])
    
    # Step 5: Calculate compressed length
    compressed_length = sum(1 + (segment[1] > 1) for segment in unique_segments)  # 1 for value, 1 extra if count > 1
    
    # Step 6: Additional transformation using frozenset operations
    base_pairs = frozenset(['A', 'T'])
    gc_pairs = frozenset(['G', 'C'])
    segment_nucleotides = {nucleotide for nucleotide, _ in unique_segments}
    
    # Adjust compressed_length based on nucleotide composition
    if segment_nucleotides.issubset(base_pairs):
        compressed_length *= 2
    elif segment_nucleotides.issubset(gc_pairs):
        compressed_length *= 3
    else:
        compressed_length += len(segment_nucleotides)
    
    return compressed_length

# Execute the pipeline
sample_sequence = "AAACCCTTTGGGAAATTTGGGCCC"
compressed_length = process_genomic_data(sample_sequence)
print(f"Result: {compressed_length}")