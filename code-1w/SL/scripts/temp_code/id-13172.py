from collections import defaultdict, Counter
import itertools

# Simulated sensor array data (temperature, pressure, vibration)
sensor_logs = [
    (23.4, 99.1, 12), (25.1, 100.3, 15), (22.7, 98.8, 11),
    (35.6, 105.0, 45), (24.0, 99.5, 13), (26.8, 101.2, 18),
    (28.3, 102.7, 25), (30.1, 103.4, 30), (27.5, 101.8, 20),
    (29.7, 104.1, 33), (22.1, 98.0, 10), (24.8, 100.1, 14)
]

# Irrelevant baseline calibration constants (distractor)
calibration_offset = 0.87
reference_stability_index = 98.6
dummy_weights = [0.1, 0.3, 0.6]

# Misleading intermediate transformation (dead path)
def apply_calibration(data):
    return [(t + calibration_offset, p, v) for t, p, v in data]

# Unused function - red herring
def analyze_trend(sequence):
    diffs = [b - a for a, b in zip(sequence, sequence[1:])]
    return sum(diffs) / len(diffs)

# Decoy statistical summary (not used in final logic)
pressure_series = [p for _, p, _ in sensor_logs]
stable_pressures = [p for p in pressure_series if 99 <= p <= 101]
outlier_count = len([p for p in pressure_series if p > 103])

# Real processing begins here
operational_ranges = {
    'temp': (22.0, 32.0),
    'pressure': (98.5, 103.5),
    'vibration': (10, 28)
}

# Complex filtering using multiple criteria
filtered_data = []
for entry in sensor_logs:
    t, p, v = entry
    if (operational_ranges['temp'][0] <= t <= operational_ranges['temp'][1] and
        operational_ranges['pressure'][0] <= p <= operational_ranges['pressure'][1] and
        operational_ranges['vibration'][0] <= v <= operational_ranges['vibration'][1]):
        filtered_data.append(entry)

# Generate all valid trios from filtered data (irrelevant combinatorics)
valid_combinations = list(itertools.combinations(filtered_data, 3))
combination_count = len(valid_combinations)  # Distractor metric

# Build threshold map with nested logic
threshold_map = defaultdict(dict)
for sensor_type, (low, high) in operational_ranges.items():
    mid = (low + high) / 2
    threshold_map[sensor_type]['warning'] = mid
    threshold_map[sensor_type]['critical'] = high - 0.5

# Unused bitmask analysis (misdirection)
status_flags = 0
for t, p, v in filtered_data:
    flag = 0
    if t > threshold_map['temp']['warning']: flag |= 1
    if p > threshold_map['pressure']['warning']: flag |= 2
    if v > threshold_map['vibration']['warning']: flag |= 4
    status_flags ^= flag  # XOR accumulation - never used

# Real diagnostic processor
def process_readings(data, thresholds):
    stats = Counter()
    diagnostics = []
    
    for t, p, v in data:
        # Evaluate each reading against thresholds
        temp_status = 1 if t > thresholds['temp']['warning'] else 0
        press_status = 1 if p > thresholds['pressure']['warning'] else 0
        vib_status = 1 if v > thresholds['vibration']['warning'] else 0
        
        # Bitwise encoding of state (relevant operation)
        encoded_state = (temp_status << 2) | (press_status << 1) | vib_status
        stats[encoded_state] += 1
        
        # Conditional expression for health scoring
        score = 100 - (t * 0.5) if t < 30 else 60 - (v * 0.7)
        diagnostics.append(round(score, 2))
    
    # Core logic: weighted impact calculation
    total_impact = 0
    for state_code, count in stats.items():
        # Non-linear impact based on bit pattern
        severity = bin(state_code).count('1')  # Number of active warnings
        if severity == 0:
            impact = 0
        elif severity == 1:
            impact = 5 * count
        elif severity == 2:
            impact = 12 * count
        else:  # severity == 3
            impact = 25 * count
        total_impact += impact
    
    # Final aggregation using average and impact penalty
    avg_diagnostic = sum(diagnostics) / len(diagnostics) if diagnostics else 0
    final_value = avg_diagnostic - (total_impact * 0.3)
    
    return int(round(final_value))

# Critical execution point
final_diagnostic = process_readings(filtered_data, threshold_map)

# Output result as required
print(f"Result: {final_diagnostic}")