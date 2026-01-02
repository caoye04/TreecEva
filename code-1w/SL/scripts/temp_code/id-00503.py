import math

# Simulated sensor data and calibration parameters
temperature_readings = [23.5, 24.1, 22.9, 25.6, 26.0, 24.8, 23.7, 25.2]
pressure_readings = [101.3, 102.1, 100.9, 103.4, 104.0, 101.8, 103.2, 102.7]
humidity_readings = [45, 47, 50, 44, 46, 48, 52, 49]

# Irrelevant auxiliary data (distractor)
color_spectrum = ['red', 'green', 'blue', 'alpha']
fft_buffer = [0] * 16
dummy_flag = True
offset_lookup = {i: i * 1.05 for i in range(10)}

# Signal processing pipeline
def clean_noise(data, threshold=1.5):
    mean_val = sum(data) / len(data)
    filtered = [x for x in data if abs(x - mean_val) < threshold]
    return filtered if len(filtered) > 0 else [mean_val]

# Unused function - red herring
def deprecated_normalization(arr):
    min_val, max_val = min(arr), max(arr)
    return [(x - min_val) / (max_val - min_val) for x in arr]

# Misleading transformation chain
def transform_sequence(seq):
    temp_result = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            temp_result.append(val * 1.02)
        else:
            temp_result.append(val + 0.03)
    # This slicing reverses only half — misleading but not used later
    temp_result[:len(temp_result)//2] = temp_result[:len(temp_result)//2][::-1]
    return temp_result

# Core data preprocessing
raw_combined = [t * 10 + p for t, p in zip(temperature_readings, pressure_readings)]
smoothed_signal = clean_noise(raw_combined, threshold=2.0)

# Decoy computation with string manipulation (irrelevant)
status_tags = ['OK', 'ACTIVE', 'MONITORED']
operation_mode = '_'.join(status_tags).lower()
system_id = operation_mode.replace('_', '-') + '-v2'

# Conditional data selection based on length (actual use)
if len(smoothed_signal) > 6:
    working_data = smoothed_signal[1:-1]  # Remove outliers at edges
else:
    working_data = smoothed_signal

# Apply conditional scaling
scaling_factor = 1.1 if sum(working_data) > 1000 else 0.95
scaled_data = [x * scaling_factor for x in working_data]

# Bit manipulation decoy (no effect on result)
bitmask = 0b101010
masked_values = [int(x) & bitmask for x in scaled_data[:4]]

# Real processing begins: frequency emulation via trigonometric wrapping
def simulate_frequency_envelope(signal):
    envelope = []
    for i, val in enumerate(signal):
        # Simulate harmonic distortion
        harmonic = math.sin(i * 0.5) * 0.1 * val
        envelope.append(val + harmonic)
    return envelope

processed_data = simulate_frequency_envelope(scaled_data)

# Redundant sorting path (dead branch)
if any(x > 250 for x in processed_data):
    sorted_diagnostics = sorted(processed_data, reverse=True)
    median_index = len(sorted_diagnostics) // 2
    median_value = (sorted_diagnostics[median_index] + sorted_diagnostics[~median_index]) / 2
else:
    # This branch actually executes
    base_reference = sum(processed_data) / len(processed_data)
    adjusted_ref = base_reference * 0.98 if len(processed_data) % 2 == 0 else base_reference * 1.02

# Critical recursive diagnostic analyzer
def analyze_signal(data, depth=0):
    if depth >= 3 or len(data) < 2:
        return sum(data) / len(data)
    
    # Recursive decomposition using slicing
    mid = len(data) // 2
    left_half = data[:mid] if mid > 0 else data
    right_half = data[mid:] if mid < len(data) else data
    
    # Conditional recursion path
    if sum(left_half) > sum(right_half):
        next_depth = depth + 1
        return analyze_signal([x * 0.97 for x in left_half], next_depth)
    else:
        # This branch taken — key to final answer
        return analyze_signal([x * 1.03 for x in right_half], depth + 1)

# Final computation
final_diagnostic = analyze_signal(processed_data)

# Print required output
print(f"Result: {final_diagnostic}")