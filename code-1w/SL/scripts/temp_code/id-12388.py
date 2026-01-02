def preprocess_signal(raw_data, threshold=0.75):
    """Irrelevant preprocessing function (dead code path)"""
    filtered = [x for x in raw_data if abs(x) > threshold]
    return [x * 1.05 for x in filtered]


def compute_entropy(sequence):
    """Unused entropy calculation (distractor)"""
    from math import log
    freq = {}
    for item in sequence:
        freq[item] = freq.get(item, 0) + 1
    total = len(sequence)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        entropy -= p * log(p)
    return entropy

# Simulated quantum sensor readings (mixed valid and noise data)
quantum_readings = [
    1.2, -0.8, 3.4, 2.1, 0.5, 1.9, 4.4, 1.1, 2.3, 3.7,
    0.6, 1.8, 2.9, 3.3, 1.4, 2.5, 3.6, 2.2, 1.7, 0.9
]

# Calibration map with decoy keys and irrelevant mappings
 calibration_map = {
    'baseline': 1.0,
    'gain': 1.25,
    'offset_qx7': 0.15,
    'threshold_anomaly': 3.0,
    'legacy_mode': False,
    'debug_trace': [],
    'version': '2.1a',
    'scale_factor': 0.95
}

# Irrelevant signal mask (unused)
signal_mask = [i for i, v in enumerate(quantum_readings) if v > 0.5]

# Decoy diagnostic matrix (looks important but unused)
diag_matrix = [[i+j for j in range(5)] for i in range(5)]

# Auxiliary lookup table using enumerate and zip (partially relevant)
index_weights = {i: w for i, w in enumerate([0.8, 1.1, 0.9, 1.2, 1.0])}
shift_labels = ['A', 'B', 'C', 'D', 'E']
label_mapping = dict(zip(shift_labels, [100, 200, 300, 400, 500]))

# Secondary processing with red herring operations
temp_buffer = []
for idx, reading in enumerate(quantum_readings):
    adjusted = reading * calibration_map['gain']
    if adjusted > calibration_map['threshold_anomaly']:
        temp_buffer.append((idx, adjusted))
    
    # Dead logic branch (never reached due to structure)
    if reading < 0 and calibration_map.get('legacy_mode'):
        temp_buffer.append((-1, -999))

# Real computation begins here (buried among distractors)
effective_values = []
for val in quantum_readings:
    if val >= 1.5:
        scaled = val * calibration_map['scale_factor']
        rounded = int(scaled + 0.5)  # Integer rounding
        effective_values.append(rounded)

# Key transformation: frequency counting via dictionary
freq_count = {}
for v in effective_values:
    freq_count[v] = freq_count.get(v, 0) + 1

# Conditional override based on comparison (relevant logic)
if len(effective_values) > 10:
    cap_limit = 3
    capped_freq = {k: min(v, cap_limit) for k, v in freq_count.items()}
else:
    capped_freq = freq_count

# Final aggregation with case conversion red herring
mode_flag = 'ENABLED'
flag_code = mode_flag.lower()  # Looks like config parsing

# Core algorithm: sum of key-adjusted frequencies
aggregate = 0
for key, count in capped_freq.items():
    if key % 2 == 0:  # even keys get doubled weight
        aggregate += count * 2
    else:
        aggregate += count * 1

# Secondary adjustment based on calibration offset (only this part used)
final_diagnostic = aggregate + int(calibration_map['offset_qx7'] * 100)

# Spurious print calls (distraction)
print(f"Signal mask: {signal_mask[:3]}...")
print(f"Diagnostic matrix shape: 5x5")
print(f"Processing mode: {flag_code}")

# Critical output line (must be present)
Target result: {final_diagnostic}