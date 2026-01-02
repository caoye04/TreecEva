import itertools

# System health monitoring simulation with diagnostic computation

def preprocess_signals(raw_readings):
    filtered = [x for x in raw_readings if abs(x) > 0.1]
    normalized = [(x - min(filtered)) / (max(filtered) - min(filtered)) for x in filtered]
    return [round(n * 100) for n in normalized]

# Irrelevant helper - distractor
def compute_entropy(data):
    from math import log
    freq = {}
    for d in data:
        freq[d] = freq.get(d, 0) + 1
    total = len(data)
    return sum(-(count/total) * log(count/total) for count in freq.values())

# Unused transformation - dead code path
def legacy_transform(seq):
    return [seq[i] ^ seq[(i+1)%len(seq)] for i in range(len(seq))]

# Core processing function with red herrings
def generate_timing_profile(base_sequence, shift_offset=3):
    shifted = [(x + shift_offset) % 256 for x in base_sequence]
    paired = list(itertools.zip_longest(shifted, [x*2 for x in shifted], fillvalue=1))
    flattened = [item for pair in paired for item in pair]
    # Real usage begins here
    checksum = sum(flattened[::3]) % 100
    metadata_tag = (checksum ^ 97) + 5
    return flattened, metadata_tag

# Decoy function that looks important but is never called
def audit_trail(events, keylog=None):
    if keylog:
        return {k: events.count(k) for k in set(events)}
    else:
        return {'audit_failed': True}

# Another irrelevant utility - adds distraction
class DataObfuscator:
    def __init__(self, seed=1):
        self.mask = [seed * (i+1) % 255 for i in range(10)]

    def scramble(self, data):
        return [d ^ self.mask[i % 10] for i, d in enumerate(data)]

# Real computational chain starts here
raw_sensor_data = [0.15, 0.4, 0.08, 0.22, 0.31, 0.03, 0.55, 0.19]
calibration_matrix = [[1.1, 0.9], [0.8, 1.2], [1.0, 1.0]]

# Step 1: Preprocess signal readings
cleaned_data = preprocess_signals(raw_sensor_data)

# Step 2: Generate timing profile
sequence_input = [sum(cleaned_data)//len(cleaned_data), 42, 64]
timing_data, tag = generate_timing_profile(sequence_input)

# Step 3: Simulate buffer alignment
alignment_shift = tag % 7
timing_data = [t ^ alignment_shift for t in timing_data]

# Step 4: Extract diagnostic windows
window_a = timing_data[5:12]
window_b = timing_data[8:15]
overlap_xor = [a ^ b for a, b in zip(window_a, window_b)]

# Step 5: Compute interference pattern (red herring)
interference_pattern = []
for i in range(len(overlap_xor)):
    val = overlap_xor[i]
    if i % 2 == 0:
        val = (val + 17) % 256
    else:
        val = (val * 3) % 256
    interference_pattern.append(val)

# Step 6: Actual relevant logic - frequency analysis
freq_map = {}
for v in interference_pattern:
    freq_map[v] = freq_map.get(v, 0) + 1

# Step 7: Aggregate metrics using only specific keys
active_codes = [k for k, v in freq_map.items() if v >= 2]
base_score = sum(active_codes)

# Step 8: Use string method as subtle transformation
hex_rep = ''.join([hex(base_score)[2:], hex(tag)[2:]])
digit_sum = sum(int(c) for c in hex_rep if c.isdigit())

# Step 9: Final diagnostic calculation
scaling_factor = len(calibration_matrix) * 0.5
correction_term = len(interference_pattern) // 4
final_diagnostic = int((base_score + digit_sum) * scaling_factor - correction_term)

# Step 10: Print result for evaluation
Result: {final_diagnostic}