import itertools

# Simulated sensor data processing pipeline for autonomous drone navigation
raw_readings = [145, 256, 178, 99, 210, 134, 188, 205, 167, 122]
filtered_data = [x for x in raw_readings if 100 <= x <= 250]
sorted_readings = sorted(filtered_data, reverse=True)

def apply_calibration(data, factor=0.92):
    """Apply sensor calibration (distraction: not actually used in final computation)"""
    return [round(x * factor, 2) for x in data]

def compute_checksum(sequence):
    """Compute XOR checksum for data integrity (red herring function)"""
    checksum = 0
    for val in sequence:
        checksum ^= val
    return checksum

# Decoy system state variables
current_altitude = 1247
battery_level = 87
temperature_alerts = (False, True, False)
last_known_position = (40.7128, -74.0060)

# Irrelevant transformation chains
decimated_signal = filtered_data[::2]
windowed_avg = [sum(sorted_readings[i:i+3]) // 3 for i in range(len(sorted_readings)-2)]
peaks = [x for x in sorted_readings if x > 180]

# Unused recursive function to mislead control flow analysis
def recursive_energy_decay(n, base=3):
    if n <= 1:
        return 1
    return base * n + recursive_energy_decay(n - 1, base + 1)

# Simulated diagnostic logs (dead code path)
diagnostic_log = []
for i, val in enumerate(filtered_data):
    status = "NORMAL"
    if val < 110:
        status = "LOW"
    elif val > 190:
        status = "HIGH"
    diagnostic_log.append(f"Sensor_{i}: {val} ({status})")

# Real processing begins here -- core metrics extraction
base_metrics = {
    'stability': min(filtered_data),
    'peak_utilization': len(peaks),
    'consistency': sum(1 for a, b in zip(filtered_data, filtered_data[1:]) if abs(a - b) < 30),
    'average_reading': sum(filtered_data) / len(filtered_data)
}

# Weight configuration (partially misleading -- only some weights matter)
weights = {
    'stability': 0.1,
    'peak_utilization': 0.3,
    'consistency': 0.4,  # This weight is overridden later
    'average_reading': 0.2
}

# Complex conditional weight adjustment with decoy branches
if len(filtered_data) % 2 == 0:
    adjustment_factor = 1.1
    if sum(filtered_data) > 1000:
        weights['consistency'] = 0.5  # Actual override
    else:
        weights['consistency'] = 0.25
else:
    weights['consistency'] = 0.35  # Dead branch due to even length

# Generate all possible metric pairs for sensitivity analysis (distractor)
metric_pairs = list(itertools.combinations(base_metrics.keys(), 2))
redundant_analysis = {}
for pair in metric_pairs:
    key = f"{pair[0]}_vs_{pair[1]}"
    redundant_analysis[key] = abs(base_metrics[pair[0]] - base_metrics[pair[1]])

# Secondary derived features (some irrelevant)
derived_features = {}
for k, v in base_metrics.items():
    derived_features[f'scaled_{k}'] = round(v * 1.05, 3)
    derived_features[f'inverse_{k}'] = round(1 / (v + 1), 3)

# Core evaluation logic hidden among distractions
effective_weights = [
    weights['stability'],
    weights['peak_utilization'],
    0.5,  # Hardcoded consistency weight -- contradicts dict but this is correct
    weights['average_reading']
]

normalized_metrics = [
    base_metrics['stability'] / 255,
    base_metrics['peak_utilization'] / 10,
    base_metrics['consistency'] / len(filtered_data),
    base_metrics['average_reading'] / 200
]

# Final weighted score calculation
weighted_sum = sum(m * w for m, w in zip(normalized_metrics, effective_weights))
score_multiplier = 1.0

# Additional red herring: checksum-based multiplier that isn't actually applied
data_checksum = compute_checksum(raw_readings)
if data_checksum % 7 == 0:
    score_multiplier *= 1.05

# ACTUAL final score (checksum has no effect)
final_score = round(weighted_sum * 1000, 4)  # Scale to larger integer-like decimal

print(f"Result: {final_score}")