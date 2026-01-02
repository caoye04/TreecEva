def preprocess_sequence(seq):
    return [x for x in seq if x % 3 != 0]

# Irrelevant helper function (dead code path)
def encrypt_payload(data):
    return sum([d ^ 255 for d in data])

# Another decoy transformation
def transform_signal(signal):
    shifted = [(s << 2) & 255 for s in signal]
    return [s ^ 170 for s in shifted]

# Misleading intermediate calculation
tamper_resistant_id = 0
for i in range(12):
    tamper_resistant_id += (i * 17) % 97
tamper_resistant_id = (tamper_resistant_id * 31) % 65537

# Core data structures
log_entries = list(range(100, 116))  # Simulated log IDs
access_keys = ['alpha', 'beta', 'gamma', 'delta', 'epsilon']

# Distractor: unused but plausible-looking mapping
key_mapping = {k: idx * 19 for idx, k in enumerate(access_keys)}

# Distractor computation with string methods
fingerprint = ''.join([k[0].upper() + str(len(k)) for k in access_keys])
fingerprint_hash = sum([ord(c) * (i + 1) for i, c in enumerate(fingerprint)])

# Real work begins: filter and transform logs
filtered_logs = preprocess_sequence(log_entries)
modded_logs = [l % 13 for l in filtered_logs]

# Use of enumerate and zip (required feature)
indexed_weights = {}
for idx, val in enumerate(modded_logs):
    indexed_weights[idx] = val * (idx + 1)

weight_keys = list(indexed_weights.keys())[:len(access_keys)]
paired_data = list(zip(weight_keys, [len(k) for k in access_keys]))

# Secondary transformation chain
aggregated = 0
for pair in paired_data:
    key_part, len_part = pair
    aggregated += (key_part * len_part) ^ 5

# Decoy state accumulator (never used)
consistency_trace = []
for _ in range(4):
    consistency_trace.append(aggregated % 256)
    aggregated = (aggregated // 7) + 13

# Actual critical computation path
shift_register = 1
for val in modded_logs:
    shift_register = (shift_register * val + 3) % 997

# Character counting distraction
description = "System integrity verification layer"
char_count = {c: description.count(c) for c in set(description) if c.isalpha()}
letter_sum = sum([v for v in char_count.values() if v % 2 == 1])

# Final checksum built from multiple sources but only some matter
temp_key = 0
for i, c in enumerate(fingerprint):
    if c.isdigit():
        temp_key += int(c) * (i + 1)

# Critical statement
final_checksum = compute_integrity_value(log_entries, access_keys)

# Top-level function definition must come last due to dependency
def compute_integrity_value(entries, keys):
    base_seq = [e % 11 for e in entries if e % 2 == 0]  # Only even logs mod 11
    offset = len(keys) * 2
    result = offset
    for i, b in enumerate(base_seq):
        result += b * (i + 1)
    # Incorporate bit manipulation
    result = (result ^ 0xF0F0) & 0xFFFF
    # Add modular contribution from string lengths
    length_mod = sum([len(k) for k in keys]) % 8
    result = (result + (length_mod * 17)) % 100000
    return result

# Ensure function is called after definition
final_checksum = compute_integrity_value(log_entries, access_keys)
print(f"Target result: {final_checksum}")