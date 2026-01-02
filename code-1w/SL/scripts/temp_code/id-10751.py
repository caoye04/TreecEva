from itertools import combinations

# Simulate data packet processing with integrity check
raw_data = [123, 45, 67, 89, 12, 34, 56, 78]
key_offset = 17
noise_sequence = [i % 13 for i in range(len(raw_data))]

# Irrelevant transformation: string manipulation distraction
temp_str = ''.join([chr((x + key_offset) % 90 + 33) for x in raw_data])
filtered_chars = [c for c in temp_str if c.isalpha()]
scrambled = temp_str[::-1].lower().replace('a', 'z')  # Unused distractions

# Real computation begins
weighted_vals = [(val * (i + 1)) for i, val in enumerate(raw_data)]
summed_pairs = [sum(pair) for pair in combinations(weighted_vals[:4], 2)]

# Accumulate relevant values
running_total = 0
bit_accumulator = 0
for idx, wv in enumerate(weighted_vals):
    running_total += wv
    bit_accumulator ^= (wv << 1) | (idx & 1)
    
    # Dead code path - never executed due to fixed condition
    if len(noise_sequence) < 0:
        running_total -= 1000

# Secondary distraction: unused advanced slicing
window_slices = [weighted_vals[i:i+3] for i in range(0, len(weighted_vals), 2)]
overlap_sum = sum([slice_val[0] for slice_val in window_slices if len(slice_val) > 1])

# Core logic hidden among distractions
baseline = sum(raw_data) + key_offset
scaling_factor = len(filtered_chars) if filtered_chars else 4  # Depends on earlier string op
intermediate = running_total + (baseline // scaling_factor)

# Final summation using composite calculation
final_sum = intermediate

# Key statement
checksum = final_sum ^ (bit_accumulator & 255)

print(f"Result: {checksum}")