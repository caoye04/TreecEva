import itertools

def rotate_bits_left(val, n, width=8):
    return ((val << n) | (val >> (width - n))) & ((1 << width) - 1)

def calculate_entropy(chunk):
    freq_map = {}
    for b in chunk:
        freq_map[b] = freq_map.get(b, 0) + 1
    entropy = 0
    total = len(chunk)
    for count in freq_map.values():
        p = count / total
        entropy -= p * (p).bit_length()  # Simplified info content
    return round(entropy, 4)

def process_segment(segment):
    temp_sum = 0
    xor_fingerprint = 0
    shifted_vals = []
    
    for i, val in enumerate(segment):
        if i % 2 == 0:
            temp_sum += val ** 2
        else:
            temp_sum -= val
        
        # Core transformation
        rotated = rotate_bits_left(val, 3)
        xor_fingerprint ^= rotated
        
        # Distractor: irrelevant accumulation
        if val > 50:
            shifted_vals.append(rotated % 17)
    
    # Secondary distractor: unused entropy-like calc
    _ = calculate_entropy(segment)
    
    # Real contribution to result
    base_score = temp_sum & 0xFF
    final_hash = base_score ^ xor_fingerprint ^ (len(segment) << 2)
    
    return final_hash

# Simulate data segments from sensor array
raw_data_stream = list(itertools.chain(
    [12, 88, 45, 13],
    [97, 23, 66, 19],
    [31, 74, 58, 42],  # target segment
    [88, 11, 99]
))

# Segment extraction (distractor: multiple unused segments)
segments = []
cursor = 0
for size in [4, 4, 4, 3]:
    segments.append(raw_data_stream[cursor:cursor+size])
    cursor += size

# Auxiliary analysis (dead code path - not used later)
diagnostic_modes = []
for s in segments:
    mode_val = max(set(s), key=s.count) if len(set(s)) < len(s) else 0
    diagnostic_modes.append(mode_val)

# Primary computation with key intervention point
running_diagnostic = 0
for seg in segments[:3]:
    running_diagnostic += sum(seg) // len(seg)

# Key assignment - target execution point
final_checksum = process_segment(segments[2])

# Additional noise: unused transformation chain
shadow_buffer = [x ^ 0xAA for x in raw_data_stream if x < 70]
scratch_result = sum(shadow_buffer[i] << 1 for i in range(0, len(shadow_buffer), 3)) if shadow_buffer else 0

print(f"Result: {final_checksum}")