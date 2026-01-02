from itertools import combinations

# Simulate secure key derivation with noise masking
def derive_key_segments(seed_value):
    segment_a = (seed_value * 17 + 13) % 256
    segment_b = (seed_value * 23 + 19) % 256
    segment_c = (seed_value * 31 + 29) % 256
    return segment_a, segment_b, segment_c

def analyze_pattern(seq):
    count = 0
    for a, b in combinations(seq, 2):
        if (a ^ b) & 1:
            count += 1
    return count

seed_input = 42
base_segments = derive_key_segments(seed_input)

# Misleading transformation chain (some irrelevant)
dummy_transform = [(x * 7 + 3) % 256 for x in base_segments]
filtered_values = [x for x in dummy_transform if x > 50]
masked_set = set(filtered_values)
distraction_sum = sum(masked_set) // len(masked_set) if masked_set else 0

# Real processing begins
working_list = list(base_segments)
working_list.append(working_list[0] ^ working_list[1])

# Apply string-based filtering (semi-relevant)
status_flag = 'active'
suffix_score = len(status_flag.upper().strip()) * 2

if status_flag in ['active', 'debug']:
    working_list.append(suffix_score)

# Nested logic with early exit
intermediate = 0
temp_checksum = 0
for idx, val in enumerate(working_list):
    if val % 2 == 0:
        intermediate += val * 3
    else:
        intermediate -= val
    
    if intermediate > 100:
        intermediate = intermediate % 73
        break  # Early termination possible but not triggered here

# Core checksum computation
checksum = 53
for v in working_list:
    checksum ^= v

final_key = working_list[-1] + (len(working_list) & 15)
checksum = (checksum << 1) ^ final_key  # Key statement

# Additional red herring computations (no effect on result)
padding_block = [checksum & 0xFF, (checksum >> 8) & 0xFF]
reconstructed = padding_block[0] + (padding_block[1] << 8)
analysis_pairs = list(combinations(padding_block, 2))

# Output the target variable
print(f"Result: {checksum}")