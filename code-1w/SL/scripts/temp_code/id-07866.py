import math

# Simulated sensor data from industrial monitoring system
turbine_readings = [384, 291, 450, 127, 503, 215, 344, 410, 276, 330]
ambient_temps = [22.1, 23.5, 21.8, 24.0, 22.7, 23.1, 21.9, 24.2, 22.4, 23.0]

# Irrelevant calibration constants (distractors)
CALIBRATION_FACTOR_X = 0.987
REFERENCE_OFFSET_Y = 1.023
MAX_TOLERANCE_Z = 0.005

# Preprocessing: filter anomalies using threshold logic
def filter_anomalies(data, threshold=350):
    return [x for x in data if x > threshold]  # Only high-stress readings

# Secondary processing: map to diagnostic categories
def categorize_stress(value):
    if value < 200:
        return 'LOW'
    elif value < 400:
        return 'MODERATE'
    else:
        return 'HIGH'

# Unused decoy function – looks relevant but never called
def legacy_normalize(arr):
    max_val = max(arr)
    return [round(x / max_val, 4) for x in arr]

# Another decoy: complex transformation not used in main flow
def spectral_weight(readings):
    weighted = 0
    for i, r in enumerate(readings):
        weighted += r * math.sin(i * math.pi / 4)
    return round(weighted, 3)

# Misleading intermediate calculation (dead end)
baseline_avg = sum(turbine_readings) // len(turbine_readings)  # Integer division
adjustment_factor = math.log(baseline_avg, 10)  # Not actually used later

# Real processing begins here
filtered_readings = filter_anomalies(turbine_readings)
categorized_levels = [categorize_stress(x) for x in filtered_readings]

# Simulate timestamp alignment with ambient data (partial match)
timestamp_aligned = []
for i in range(min(len(filtered_readings), len(ambient_temps))):
    temp_offset = ambient_temps[i] - 22.0
    adjusted_reading = filtered_readings[i] - int(temp_offset * 10)
    timestamp_aligned.append(adjusted_reading)

# Decoy list comprehension – computes but doesn't affect outcome
shadow_copy = [x * 2 for x in timestamp_aligned if x < 400]

# Compute stress indices using adjusted values
stress_indices = []
for val in timestamp_aligned:
    index = int((val - 300) * 1.5)
    stress_indices.append(max(1, index))  # Clamp to minimum 1

# Additional irrelevant structure: unused dictionary mapping
diagnostic_map = {
    'HIGH': {'priority': 1, 'action': 'inspect'},
    'MODERATE': {'priority': 2, 'action': 'monitor'},
    'LOW': {'priority': 3, 'action': 'ignore'}
}

# Real work: aggregate diagnostic score
rolling_diagnostics = []
for idx, s_idx in enumerate(stress_indices):
    # Introduce decay factor based on position
    decay = 0.9 ** idx
    contribution = s_idx * decay
    rolling_diagnostics.append(round(contribution))

# Accumulate total signal strength
signal_sum = 0
weight_accum = 0.0
for i, contrib in enumerate(rolling_diagnostics):
    weight = 0.95 ** i
    signal_sum += contrib * weight
    weight_accum += weight

weighted_diagnostic = signal_sum / weight_accum if weight_accum > 0 else 0

# Final analysis function
def analyze_readings(logs):
    if not logs:
        return -1
    
    # Red herring: sort and reverse for no effect
    sorted_logs = sorted(logs)
    reversed_logs = sorted_logs[::-1]
    
    # Actual computation: median of top half
    mid = len(reversed_logs) // 2
    top_half = reversed_logs[:mid] if mid > 0 else [reversed_logs[0]]
    
    # Use floating point precision then truncate
    raw_median = sum(top_half) / len(top_half)
    base_score = int(raw_median)
    
    # Apply fake correction that cancels out
    corrected = base_score + 5 - 5
    
    # One final adjustment based on length parity
    if len(logs) % 2 == 1:
        return corrected + 10
    else:
        return corrected + 5

# Processed logs used in final call
processed_logs = timestamp_aligned.copy()

# Key assignment statement
final_diagnostic = analyze_readings(processed_logs)

print(f"Result: {final_diagnostic}")