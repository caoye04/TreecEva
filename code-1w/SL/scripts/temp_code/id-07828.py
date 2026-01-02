import itertools

# Simulated sensor data processing with noise filtering and diagnostics
raw_readings = [127, 255, 192, 64, 224, 31, 88, 176]
threshold = 128
calibration_offset = -5

# Irrelevant statistical tracking (distractor)
mean_reading = sum(raw_readings) / len(raw_readings)
variance_proxy = sum((x - mean_reading) ** 2 for x in raw_readings)
entropy_approximation = 0.0
for r in raw_readings:
    if r > 0:
        entropy_approximation += r * math.log(r, 2)

# Real signal detection: extract high-magnitude signals
high_signals = [r for r in raw_readings if r >= threshold]

# Bit-level analysis of significant signals (relevant path)
signal_patterns = []
for val in high_signals:
    binary_rep = bin(val)[2:].zfill(8)
    ones_count = binary_rep.count('1')
    parity_bit = ones_count % 2
    signal_patterns.append((val, ones_count, parity_bit))

# Decoy function - looks important but unused (dead code path)
def compute_health_index(data):
    weighted = [d * 0.95 for d in data]
    return sum(weighted) / len(weighted)

# Noise mask generation from low signals (partially irrelevant)
low_signals = [r for r in raw_readings if r < threshold]
noise_mask = 0
for ns in low_signals:
    noise_mask ^= ns  # Cumulative XOR (red herring)

# Core diagnostic logic chain
pattern_sum = sum(p[1] for p in signal_patterns)  # total bit counts
control_flag = any(p[2] == 0 for p in signal_patterns if p[0] > 200)

# Conditional transformation based on control flag
if control_flag:
    adjusted_sum = pattern_sum * 2
else:
    adjusted_sum = pattern_sum + 10

# Dictionary-based lookup for fault codes (meaningful distractor)
fault_codes = {
    'A1': 'SensorDrift',
    'B2': 'NoiseSaturation',
    'C3': 'SyncLoss'
}
active_faults = []
if adjusted_sum > 50:
    active_faults.append('A1')
if noise_mask > 100:
    active_faults.append('B2')

# Secondary adjustment via string analysis of fault keys (irrelevant but plausible)
fault_key_chars = ''.join(fault_codes.keys())
char_frequency = {c: fault_key_chars.count(c) for c in set(fault_key_chars)}
diagnostic_weight = sum(char_frequency.values())  # Always constant, misleading

# Real correction factor derived from bitwise interactions
bit_stability = 0
for a, b in itertools.combinations(high_signals, 2):
    shared_ones = bin(a & b).count('1')
    bit_stability += shared_ones

correction_factor = bit_stability - calibration_offset

# Aggregate score built from pattern analysis
aggregate_score = adjusted_sum + len(high_signals)

# Final diagnostic fusion point
final_diagnostic = aggregate_score + correction_factor

# Output requirement
print(f"Result: {final_diagnostic}")