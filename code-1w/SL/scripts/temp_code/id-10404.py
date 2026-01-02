import itertools

# Simulated sensor array diagnostics with mixed data processing
sensor_ids = ['S1', 'S2', 'S3', 'S4']
data_packets = [127, 255, 192, 144]
threshold_mask = [x & 64 != 0 for x in data_packets]

# Irrelevant transformation chain (distractor)
encoded_tags = [bin(ord(tag[0]) << 2)[2:] for tag in sensor_ids]
decoded_shift = sum(len(tag) for tag in encoded_tags) % 8

# Real computation path begins
bit_flags = [x & 15 for x in data_packets]                    # Extract lower 4 bits
flag_sum = sum(bit_flags)                                   # 15 + 15 + 0 + 0 = 30

# Conditional adjustment based on threshold activation
dynamic_offset = 7 if any(threshold_mask) else -3           # True -> 7

# Secondary distraction: unused complex structure
combinations = list(itertools.combinations(data_packets, 2))
checksum_pairs = sum(a ^ b for a, b in combinations) // 10   # Dead-end calculation

# Data normalization via distractor function
def normalize(value, scale=10):
    return (value % scale) * 1.5

# Unused normalization chain
normalized_flags = [normalize(flag, 8) for flag in bit_flags]  # [3.0, 3.0, 0.0, 0.0] - irrelevant

# Core logic embedded in noise
aggregate_score = flag_sum * dynamic_offset                 # 30 * 7 = 210

# Decoy variables with plausible names
baseline_reference = 210
reference_matched = (baseline_reference == aggregate_score)
validation_tier = reference_matched and aggregate_score > 200

# More distractions: string-based flag analysis
status_map = {True: 'ACTIVE', False: 'IDLE'}
sensor_states = [status_map[ref > 128] for ref in data_packets]  # ['ACTIVE', 'ACTIVE', 'IDLE', 'IDLE']
active_count = sensor_states.count('ACTIVE')                  # 2 - misleading relevance

# Correction factor derived from bitwise pattern analysis
correction_source = data_packets[0] ^ data_packets[3]         # 127 ^ 144 = 27
correction_factor = (correction_source & 31) - 5              # 27 & 31 = 27; 27 - 5 = 22

# Final diagnostic computation (target)
final_diagnostic = aggregate_score + correction_factor        # 210 + 22 = 232

# Red herring: conditional override that never triggers
if all(x < 100 for x in bit_flags):
    final_diagnostic *= 0.5  # Never executed

# Output target result
print(f"Result: {final_diagnostic}")