import itertools

# Simulated sensor data processing with diagnostic analysis
raw_readings = [0.88, -1.22, 3.14, -2.71, 0.0, 1.41, -1.73, 2.23]
timestamp_flags = [True, False, True, True, False, True, False, True]

# Irrelevant auxiliary variables (distractors)
calibration_offset = 0.05
reference_map = {i: chr(65 + i % 26) for i in range(50)}
buffer_pool = list(itertools.permutations([1, 2, 3], 3))
device_status_log = ['OK', 'RETRY', 'FAIL', 'PENDING'] * 10

# Preprocessing stage 1: normalize and filter
normalized = []
for val in raw_readings:
    if abs(val) >= 1.0:
        normalized.append(round(val ** 2 / 3.0, 6))
    else:
        normalized.append(round(abs(val) * 0.5, 6))

# Dead code path - never executed due to constant guard (red herring)
special_encoding = None
if len(normalized) < 5:
    special_encoding = ''.join([f'{x:.2f}' for x in normalized])

# Preprocessing stage 2: pair with flags and transform
paired_data = [(n, f) for n, f in zip(normalized, timestamp_flags)]
processed_data = []

for idx, (val, flag) in enumerate(paired_data):
    if flag:
        # Apply conditional transformation based on index parity
        if idx % 2 == 0:
            transformed = val * 1.5
        else:
            transformed = val + 0.75
        processed_data.append(transformed)
    else:
        # Decoy operation: scaled but unused
        dummy_scaled = val * 0.1
        processed_data.append(val)  # Still use original

# Extraneous string manipulation (distractor)
status_summary = "Analysis:" + "_".join(device_status_log[:5])
diagnostic_token = status_summary.split(':')[1].replace('_', '').lower()
hash_value = sum(ord(c) for c in diagnostic_token) % 100

# Real computation path begins here — subtle due to noise
intermediate_signal = 0.0
for x in processed_data:
    if x > 1.0:
        intermediate_signal += x * 0.9
    elif x < 0.5:
        intermediate_signal -= 0.2
    else:
        intermediate_signal += 0.1

# Conditional expression with bit manipulation red herring
bit_noise = 0
for i in range(8):
    bit_noise ^= i << 1  # Computationally irrelevant

# Core logic hidden among distractions
threshold_met = intermediate_signal > 2.0

# Unused recursive decoy function (dead definition)
def evaluate_health(rec_level, data):
    if rec_level == 0 or not data:
        return sum(data) if data else 0
    return evaluate_health(rec_level - 1, data[1:]) + data[0]

# Actual analysis function (only one that matters)
def analyze_signal(signal_list):
    base_score = sum(signal_list)
    penalty = 0
    
    # Additional logic steps
    for s in signal_list:
        if s > 2.0:
            penalty += 0.3
        elif s < 0.3:
            penalty -= 0.1  # Negative penalty bonus
    
    adjustment = len([x for x in signal_list if x > 1.0]) * 0.05
    
    # Final formula
    result = base_score - penalty + adjustment
    
    # Secondary correction based on global threshold
    if threshold_met:
        result *= 1.1
    
    return round(result, 6)

# Critical execution point
final_diagnostic = analyze_signal(processed_data)

# Output required format
print(f"Result: {final_diagnostic}")