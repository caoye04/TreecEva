from contextlib import contextmanager
from collections import namedtuple
import struct

def decode_dna_sequence(encoded_bytes):
    # Convert bytes to binary string
    binary_str = ''.join(format(byte, '08b') for byte in encoded_bytes)
    # Decode 2-bit codes to nucleotides
    mapping = {'00': 'A', '01': 'T', '10': 'G', '11': 'C'}
    nucleotides = []
    for i in range(0, len(binary_str)-1, 2):
        code = binary_str[i:i+2]
        if code in mapping:
            nucleotides.append(mapping[code])
    return ''.join(nucleotides)

def encode_dna_sequence(sequence):
    # Encode nucleotides to 2-bit codes then to bytes
    mapping = {'A': '00', 'T': '01', 'G': '10', 'C': '11'}
    binary_str = ''.join(mapping.get(nuc, '00') for nuc in sequence)
    # Pad to make length multiple of 8
    padding = (8 - len(binary_str) % 8) % 8
    binary_str += '0' * padding
    # Convert to bytes
    bytes_list = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        bytes_list.append(int(byte, 2))
    return bytes(bytes_list)

@contextmanager
def dna_analysis_context(batch_data):
    # Setup phase
    AnalysisResult = namedtuple('AnalysisResult', ['mutations', 'patterns', 'score'])
    processed_batches = []
    try:
        yield processed_batches
    finally:
        # Teardown phase - calculate final score
        global final_score
        total_score = 0
        unique_patterns = set()
        for result in processed_batches:
            total_score += result.score
            unique_patterns.update(result.patterns)
        # Final calculation combines total score with unique pattern count
        final_score = total_score ^ len(unique_patterns)

def find_mutation_pattern(sequence, pattern_length=3):
    patterns = set()
    for i in range(len(sequence) - pattern_length + 1):
        pattern = sequence[i:i+pattern_length]
        # Only count patterns that contain at least one mutation indicator (G or C)
        if 'G' in pattern or 'C' in pattern:
            patterns.add(pattern)
    return patterns

# Main analysis pipeline
encoded_batch = [b'\x96\xA5', b'\xCC\x33']

with dna_analysis_context(encoded_batch) as results:
    for i, encoded_seq in enumerate(encoded_batch):
        # Step 1: Decode sequence
        sequence = decode_dna_sequence(encoded_seq)
        
        # Step 2: Find mutation patterns
        mutations = find_mutation_pattern(sequence)
        
        # Step 3: Calculate base score using bitwise operations
        base_score = (len(sequence) << 2) & 0xFF
        
        # Step 4: Adjust score based on mutation count
        mutation_factor = len(mutations) | 0x0F
        adjusted_score = base_score ^ mutation_factor
        
        # Step 5: Create result object
        result = namedtuple('BatchResult', ['mutations', 'patterns', 'score'])(
            mutations=len(mutations),
            patterns=frozenset(mutations),
            score=adjusted_score
        )
        results.append(result)

print(f"Result: {final_score}")