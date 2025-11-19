from itertools import combinations
from collections import defaultdict

# Network packet analysis for covert channel detection
packet_sequences = [
    [0x41, 0x2B, 0x7F, 0x3C],
    [0x55, 0x1A, 0x6E, 0x2D],
    [0x69, 0x09, 0x5D, 0x1E]
]

# Rotating key mask for XOR operations
key_mask = [0xAA, 0x55, 0xCC, 0x33]

# Initialize signal tracking
signal_tracker = defaultdict(int)

# Process each packet sequence
for seq_idx, sequence in enumerate(packet_sequences):
    # Apply XOR transformation with rotating key
    transformed_seq = []
    for i, byte_val in enumerate(sequence):
        masked_byte = byte_val ^ key_mask[i % len(key_mask)]
        transformed_seq.append(masked_byte)
    
    # Generate all 3-byte combinations from transformed sequence
    combo_count = 0
    for combo in combinations(transformed_seq, 3):
        # Calculate combination signature using bitwise operations
        combo_signature = (combo[0] & combo[1]) | (combo[1] ^ combo[2])
        # Shift signature based on sequence position
        shifted_signature = combo_signature << (seq_idx + 1)
        signal_tracker[shifted_signature] += 1
        combo_count += 1
    
    # Update tracker with sequence metrics
    signal_tracker[seq_idx] ^= combo_count

# Calculate final covert signal strength
covert_signal_strength = 0
for key, count in signal_tracker.items():
    # Apply complex bitwise aggregation
    covert_signal_strength ^= (key & 0xFF) * count

print(f"Result: {covert_signal_strength}")