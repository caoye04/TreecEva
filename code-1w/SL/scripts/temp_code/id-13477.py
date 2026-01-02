from collections import defaultdict, Counter

# Simulated sensor fusion system for environmental diagnostics
raw_readings = [18.3, 22.1, 19.5, 25.0, 20.4, 21.3, 17.9, 23.6]
status_flags = [True, False, True, True, False, True, True, False]

def process_phase(readings, flags):
    # Irrelevant transformation: amplitude modulation (dead path)
    modulated = [r * 1.05 for r in readings]
    normalized = [max(0, min(100, (r - 15) * 2)) for r in readings]  # Clamped scaling

    # Distractor: frequency analysis with unused result
    freq_spectrum = defaultdict(float)
    for i, val in enumerate(normalized):
        freq_spectrum[i % 7] += val / (i + 1)

    # Real processing path begins
    valid_entries = []
    for i, flag in enumerate(flags):
        if flag:
            valid_entries.append(readings[i])

    # Compute moving average over valid data points
    avg_temp = sum(valid_entries) / len(valid_entries) if valid_entries else 0

    # Secondary diagnostic: variance outlier detection
    variances = [(x - avg_temp) ** 2 for x in valid_entries]
    stability_score = 100 - sum(variances)

    return avg_temp, stability_score

# Auxiliary function - never called (decoy)
def compute_fourier_components(data):
    result = []
    for k in range(len(data)):
        comp = 0
        for t, val in enumerate(data):
            comp += val * (k * t) % 8
        result.append(comp % 50)
    return result

# Unrelated string processing (distractor block)
task_label = "ENV_DIAG_001"
class_code = ''.join([c.lower() if i % 2 else c.upper() for i, c in enumerate(task_label)])
shift_key = sum([ord(c) for c in class_code]) % 11

# Bit manipulation red herring
bit_sequence = 0b110101
rotated_bits = ((bit_sequence << 3) | (bit_sequence >> 4)) & 0b11111111
hex_trace = hex(rotated_bits ^ 0xAA)

# Core logic with nested dependencies
baseline, score = process_phase(raw_readings, status_flags)

# Complex conditional mask (partially irrelevant)
threshold_mask = [1 if x > 20 else 0 for x in raw_readings]
majority_high = sum(threshold_mask) > 4

# Data grouping distraction
reading_pairs = list(zip(raw_readings, status_flags))
flag_count = Counter(flag for _, flag in reading_pairs)

# Actual critical computation chain
aggregate_score = score * 1.75

temperature_offset = baseline - 20.0
if temperature_offset > 0:
    phase_shift = 2
else:
    phase_shift = -1

# Dead code: hypothetical pressure correction
hypothetical_pressure = 1013.25
for i in range(3):
    hypothetical_pressure *= 0.987  # Not used anywhere

# Secondary decoy calculation: entropy approximation
dist = [0.1, 0.4, 0.2, 0.3]
entropy_approx = 0
for p in dist:
    if p > 0:
        entropy_approx -= p * __import__('math').log(p)

# Final diagnostic depends on multiple prior results
# This is the key statement
final_diagnostic = aggregate_score + temperature_factor * phase_shift

# temperature_factor was not defined yet — here's where it gets set (order matters)
intermediate_log = __import__('math').log(baseline * 2.1)
temperature_factor = int(intermediate_log) + (flag_count[True] // 3)

# Print final result as required
Result: {final_diagnostic}