from itertools import combinations

# Simulate packet data segments with metadata
def generate_segments():
    base_data = [12, 45, 67, 23, 89, 34]
    segments = []
    for i in range(3):
        shifted = [(x ^ i) + (i * 2) for x in base_data]
        parity = sum(shifted) % 256
        validity = len(shifted) > 5
        segments.append({'data': shifted, 'parity': parity, 'valid': validity})
    return segments

# Auxiliary function: not directly used in final result but looks relevant
def compute_legacy_sum(data):
    acc = 0
    for x in data:
        acc += (x << 1) ^ 7
    return acc % 1000

# Core processing with distractors
def process_segment(segment):
    data = segment['data']
    temp_buffer = [d * 1.5 for d in data]  # float conversion - unused later
    masked_values = [d & 0xFF for d in data]  # redundant masking (all < 256)
    
    # Red herring computation
    avg_val = sum(data) / len(data)
    deviation_score = sum(abs(x - avg_val) for x in data) / avg_val if avg_val else 0
    
    # Key logic hidden among distractions
    xor_chain = 0
    for i, val in enumerate(masked_values):
        if i % 2 == 0:
            xor_chain ^= (val + i) | 17
    
    # Secondary path that seems important but is unused
    alt_chain = 0
    for pair in combinations(data, 2):
        alt_chain += (pair[0] ^ pair[1]) % 19
    
    # Final checksum depends only on xor_chain and static offset
    final_checksum = (xor_chain + 41) % 10000
    return final_checksum

# Entry point
segments = generate_segments()

# Diagnostic block - irrelevant to final answer
for seg in segments:
    if seg['valid']:
        legacy = compute_legacy_sum(seg['data'])

# Target execution point
final_checksum = process_segment(segments[2])
print(f"Result: {final_checksum}")