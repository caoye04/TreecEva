from itertools import compress

class NucleotideEncoder:
    def __init__(self):
        self.mapping = {'A': 1, 'T': 2, 'G': 3, 'C': 4}
    
    def encode(self, sequence):
        return [self.mapping[nuc] for nuc in sequence]

def analyze_marker(seq_values):
    # Apply bitwise transformations
    transformed = []
    for i, val in enumerate(seq_values):
        if i % 2 == 0:
            transformed.append(val << 1)  # Left shift even indices
        else:
            transformed.append(val & 3)   # Bitwise AND with 3 for odd indices
    
    # Apply logical filtering using short-circuit evaluation
    valid_positions = [
        (t > 2) and (t < 10) or (t == 1) 
        for t in transformed
    ]
    
    # Extract values where valid_positions is True
    filtered_values = list(compress(transformed, valid_positions))
    
    # Calculate marker code using XOR
    marker_code = 0
    for val in filtered_values:
        marker_code ^= val
    
    return marker_code

# Main processing
encoder = NucleotideEncoder()
sequence = "ATGCAT"
encoded_sequence = encoder.encode(sequence)
marker_code = analyze_marker(encoded_sequence)
print(f"Result: {marker_code}")