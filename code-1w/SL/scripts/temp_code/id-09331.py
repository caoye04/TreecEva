import math

# Simulated sensor array data with noise and redundant metadata
data_stream = [
    {'id': 1, 'val': 3.2, 'meta': {'freq': 440, 'err': 0.01}},
    {'id': 2, 'val': -1.7, 'meta': {'freq': 880, 'err': 0.02}},
    {'id': 3, 'val': 4.5, 'meta': {'freq': 220, 'err': 0.005}},
    {'id': 4, 'val': 0.0, 'meta': {'freq': 660, 'err': 0.015}},
    {'id': 5, 'val': -2.3, 'meta': {'freq': 550, 'err': 0.01}},
    {'id': 6, 'val': 3.8, 'meta': {'freq': 330, 'err': 0.008}}
]

# Irrelevant auxiliary functions (decoy)
def analyze_frequency_spectrum(signal_list):
    return [math.sin(d['meta']['freq'] * 0.01) for d in signal_list]

# Unused transformation path
def legacy_normalize(data):
    max_val = max(abs(d['val']) for d in data)
    return [d['val'] / max_val for d in data]

# Misleading intermediate processing
temp_offsets = []
for entry in data_stream:
    offset = entry['val'] * entry['meta']['err']
    temp_offsets.append(offset)

# Real signal filtering logic begins here
deviation_threshold = 3.0
min_acceptable_val = -2.5
max_acceptable_val = 4.0

# Step 1: Filter by magnitude thresholds (control flow + comparison)
preliminary_filtered = []
for d in data_stream:
    if min_acceptable_val <= d['val'] <= max_acceptable_val:
        preliminary_filtered.append(d)

# Step 2: Remove high-deviation entries using modular consistency check
filtered_data = []
for d in preliminary_filtered:
    mod_key = int(abs(d['val'] * 10)) % 7
    if mod_key != 6:  # arbitrary exclusion rule based on digit pattern
        filtered_data.append(d['val'])

# Red herring: unused list comprehension with zip and enumerate
snapshot_indices = list(enumerate(zip([d['id'] for d in data_stream], [d['val'] for d in data_stream])))
processed_pairs = [\n    (i, val * math.cos(math.pi / (idx + 1))) \n    for i, (idx, val) in snapshot_indices if idx % 2 == 1
]

# Decoy statistical summary (never used)
mean_deviation = sum(abs(x) for x in temp_offsets) / len(temp_offsets)
peak_value = max(filtered_data)  # This looks important but isn't final

# Real computation: aggregate valid signals with calibration
def aggregate_signals(signals, calib):
    total = 0.0
    weight_sum = 0.0
    for i, sig in enumerate(signals):
        weight = (i + 1) ** 0.5  # increasing emphasis on later elements
        total += sig * weight * calib
        weight_sum += weight
    return total / weight_sum if weight_sum != 0 else 0.0

# Phantom calibration system (looks complex but only one value matters)
calibration_levels = [0.85, 0.9, 0.92, 0.95, 1.0, 1.05]
active_index = len(calibration_levels) // 2
calibration_factor = calibration_levels[active_index]  # evaluates to 0.92

# Critical statement
final_signal_strength = aggregate_signals(filtered_data, calibration_factor)

# Distractor: bit manipulation chain with no effect
bit_fiddle = int(abs(final_signal_strength * 100))
bit_fiddle ^= 0xFF
bit_fiddle &= 0x7F
bit_fiddle |= 0x20

# Output the target result
print(f"Result: {final_signal_strength}")