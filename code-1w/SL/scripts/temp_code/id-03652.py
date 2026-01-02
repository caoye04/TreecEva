from collections import defaultdict

# Simulate sensor data frames with metadata
data_frames = [
    {'id': 1, 'payload': [0x1a, 0x2f, 0x4b, 0x5c], 'seq': 101},
    {'id': 2, 'payload': [0x3e, 0x1c, 0x2a, 0x4d], 'seq': 105},
    {'id': 3, 'payload': [0x55, 0x6a, 0x7f, 0x0b], 'seq': 109},
]

# Initialize tracking and diagnostic variables
diagnostic_map = defaultdict(int)
sequence_gaps = []
expected_seq = 101
offsets = []
redundant_sum = 0

# Primary processing variables
aggregate = 0
running_offset = 0
frame_count = 0

for frame in data_frames:
    payload = frame['payload']
    current_seq = frame['seq']
    
    # Track sequence continuity (distractor: not used in final result)
    if current_seq != expected_seq:
        sequence_gaps.append((expected_seq, current_seq))
    expected_seq = current_seq + 4

    # Process each byte in payload
    for i, byte in enumerate(payload):
        # Update aggregate with XOR and rotation
        aggregate ^= (byte << (i % 3))
        aggregate = (aggregate & 0xFF) + (aggregate >> 8)  # Keep within byte range
        
        # Update running offset using arithmetic and bitwise mix
        running_offset += (byte & 0x0F) ^ (i + 1)
        
        # Diagnostic collection (irrelevant to final answer)
        key = f"group_{(byte // 16)}"
        diagnostic_map[key] += 1
        
        # Redundant accumulation (dead-end computation)
        redundant_sum += byte * (i + 1) % 7
    
    # Frame-level offset update
    frame_offset = (frame['id'] * 17) & 0x3F
    offsets.append(frame_offset)
    running_offset += frame_offset
    
    frame_count += 1

# Final checksum calculation depends only on aggregate and running_offset
final_checksum = aggregate ^ (running_offset % 256)

# Additional irrelevant transformations (distraction)
checksum_shifted = (final_checksum << 2) & 0xFF
inverted_diags = {k: 100 - v for k, v in diagnostic_map.items()}

# Output target result
Result: {final_checksum}