import itertools

# Simulated sensor data processing with diagnostic analysis
raw_readings = [0.8, 1.2, -0.5, 3.1, 2.7, -1.0, 0.3, 4.4, -2.1, 1.8]
noise_floor = 0.4
amplitude_threshold = 2.5
dampening_factor = 0.85

# Irrelevant calibration constants (distractors)
baseline_offset = 0.07
scaling_ratio = 1.03
reference_voltage = 3.3
temp_compensation = -0.02

# Misleading preprocessing path (dead code - never used)
def legacy_normalize(data):
    return [max(min(x, 1.0), -1.0) for x in data]

# Unused signal smoothing function (decoy)
def smooth_signal(signal, window=3):
    smoothed = []
    for i in range(len(signal)):
        start = max(0, i - window // 2)
        end = min(len(signal), i + window // 2 + 1)
        smoothed.append(sum(signal[start:end]) / (end - start))
    return smoothed

# Signal filtering with red herring operations
filtered_readings = []
spike_count = 0
false_alarm_risk = 0.0

for reading in raw_readings:
    # Apply noise floor filter (relevant)
    if abs(reading) > noise_floor:
        corrected = reading * dampening_factor
        filtered_readings.append(corrected)
        
        # Track high-amplitude events (partially relevant)
        if abs(corrected) > amplitude_threshold:
            spike_count += 1
    else:
        # Distractor computation (never used later)
        false_alarm_risk += 0.05 * abs(reading)

# Dead code block with misleading diagnostics
if len(filtered_readings) > 10:
    compression_rate = 0.9
    redundancy_score = 85
else:
    compression_rate = 0.6
    # Unused variable assignment
    anomaly_flag = False

# Create artificial data chunks (irrelevant grouping)
data_chunks = list(itertools.batched(filtered_readings, 2))
chunk_averages = [sum(chunk)/len(chunk) for chunk in data_chunks]

# Decoy transformation using string methods on numbers (misleading)
stringified = [str(round(x, 2)) for x in chunk_averages]
padded_strings = [s.rjust(5, '0') if '-' in s else s.zfill(5) for s in stringified]

# Real processing begins here: frequency analysis simulation
periodic_components = []
for i, val in enumerate(filtered_readings):
    # Simulate phase shift based on index (relevant)
    phase_shift = (i % 4) * 0.5
    shifted = val - phase_shift
    periodic_components.append(shifted)

# Amplitude folding via conditional expression (key step)
folded_amplitudes = [
    x if x >= 0 else -x * 0.9 for x in periodic_components
]

# Accumulate diagnostic metric using modular arithmetic (critical)
diagnostic_accumulator = 0
for idx, amp in enumerate(folded_amplitudes):
    weight = (idx + 1) % 3 + 1
    contribution = amp * weight
    diagnostic_accumulator += contribution

# Secondary processing: detect symmetry patterns (red herring)
symmetry_score = 0
for i in range(len(folded_amplitudes) // 2):
    paired_diff = abs(folded_amplitudes[i] - folded_amplitudes[-(i+1)])
    symmetry_score += 1 if paired_diff < 0.5 else 0

# Data reconstruction attempt (distractor)
reconstructed = []
for item in data_chunks:
    reconstructed.extend(item)

# Final analysis function with multiple inputs, only one actually matters
def analyze_signal(signal_data):
    base_metric = sum(signal_data) * 10
    
    # Irrelevant sub-calculations
    peak_value = max(signal_data, default=0)
    valley_count = sum(1 for x in signal_data if x < 0)
    normalized_entropy = len(signal_data) / (peak_value + 1) if peak_value else 0
    
    # Critical but non-obvious operation: use of modular accumulator
    key_index = len(signal_data) % 7
    modifier = 2.5 if key_index in [1, 3, 5] else 1.8
    
    # The real answer depends only on this line
    return int(base_metric * modifier)

# Process flow
intermediate_state = [x * 1.1 for x in folded_amplitudes]  # unused later
processed_data = [round(x, 2) for x in folded_amplitudes]

# Key execution point
final_diagnostic = analyze_signal(processed_data)

print(f"Result: {final_diagnostic}")