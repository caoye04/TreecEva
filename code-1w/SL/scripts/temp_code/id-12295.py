import math

def analyze_pattern(seq):
    # Irrelevant function: analyzes string patterns but not used in final calculation
    count = 0
    for char in seq.lower():
        if char in 'aeiou':
            count += 1
    return sorted([count, len(seq), count * 2])


def shift_buffer(data, offset):
    # Misleading transformation: looks important but unused in critical path
    return [(x + offset) % 256 for x in data]

# Decoy constants
turbulence_index = 3.14159
baseline_offset = 997
scaling_factor = 0.983

# Distractor data structures
audit_log = {
    'entries': 127,
    'status': 'verified',
    'flags': [False, True, False]
}

# Health sensor readings (simulated)
raw_readings = [23, 45, 67, 89, 12, 34, 56, 78]

# Apply irrelevant shift (dead-end computation)
shifted_readings = shift_buffer(raw_readings, baseline_offset)

# Simulate environmental noise (unused)
noise_profile = []
for i in range(len(raw_readings)):
    noise = int(math.sin(i) * 10) + 5
    noise_profile.append(noise)

# Core diagnostic parameters
threshold = 42
sample_window = (1, 6)  # indices 1 to 5 inclusive

# Primary processing pipeline
filtered_data = [x for x in raw_readings[sample_window[0]:sample_window[1]] if x > 30]

# Bit manipulation decoy
obfuscation_key = 0b101010
masked_values = [v ^ obfuscation_key for v in raw_readings]

# Conditional branching with red herring
if len(filtered_data) > 3:
    adjustment = 7
else:
    adjustment = -3

# Real computation begins here — multi-step reasoning required
aggregate = sum(filtered_data)
penalty = 0
for val in filtered_data:
    if val % 2 == 0:
        penalty += val // 10
    else:
        penalty -= val % 4

# Intermediate result disguised as final
preliminary_score = aggregate - penalty + adjustment

# String-based distractor logic
system_id = "H7X-9K2"
id_parts = system_id.split('-')
hex_part = id_parts[0][1:]  # '7X'
decoded_ref = 0
for c in hex_part:
    if c.isdigit():
        decoded_ref = decoded_ref * 16 + int(c)
    else:
        decoded_ref = decoded_ref * 16 + (ord(c.upper()) - ord('A') + 10)

# Critical: only now begin relevant conditional refinement
refined_score = preliminary_score
if preliminary_score > 100:
    refined_score = int(refined_score * 0.85)
elif preliminary_score < 50:
    refined_score = int(refined_score * 1.2)
else:
    refined_score += 5

# Now compute checksum from string ID using case conversion — actual dependency
checksum = 0
for char in system_id.replace('-', '').upper():
    if char.isalpha():
        checksum += ord(char) - ord('A') + 1
    elif char.isdigit():
        checksum += int(char)

# Final adjustment based on checksum parity and filtered size
if checksum % 2 == 0:
    final_diagnostic = refined_score + len(filtered_data)
else:
    final_diagnostic = refined_score - (len(filtered_data) // 2)

# Target result output
Result: {final_diagnostic}