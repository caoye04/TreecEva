def analyze_sequence(pattern):
    """ Analyze frequency and positional bias in a numeric pattern """
    length = len(pattern)
    midpoint = length // 2
    left_half = pattern[:midpoint]
    right_half = pattern[midpoint:]
    
    # Distractor: symmetry analysis (not used in final result)
    reversed_right = right_half[::-1]
    symmetry_match = sum(1 for i in range(len(left_half)) if left_half[i] == reversed_right[i])
    
    # Relevant: compute weighted position score
    position_weights = [i * 0.1 for i in range(length)]
    weighted_sum = sum(pattern[i] * position_weights[i] for i in range(length))
    
    # Distractor: outlier detection
    avg_val = sum(pattern) / length
    outliers = [x for x in pattern if abs(x - avg_val) > 2]
    
    return weighted_sum


def calculate_modular_trend(values, modulus=7):
    """ Calculate trend based on modular residue cycles """
    residues = [v % modulus for v in values]
    transitions = [(residues[i], residues[i+1]) for i in range(len(residues)-1)]
    
    # Count ascending modulo transitions
    asc_count = sum(1 for a, b in transitions if (b - a) % modulus == 1)
    desc_count = sum(1 for a, b in transitions if (a - b) % modulus == 1)
    
    # Distractor: transition heatmap (unused)
    heatmap = [[0]*modulus for _ in range(modulus)]
    for a, b in transitions:
        heatmap[a][b] += 1
    
    return asc_count - desc_count

# Simulate sensor benchmark data
raw_readings = [3, 7, 1, 4, 8, 2, 9, 5]
filtered_readings = [x for x in raw_readings if x > 2]  # Remove low noise
offset_correction = 0.5
adjusted_readings = [x + offset_correction for x in filtered_readings]

# Distractor: time drift simulation (irrelevant)
time_drift_log = []
current_drift = 0.0
for i in range(3):
    current_drift += 0.1 * (-1)**i
    time_drift_log.append(round(current_drift, 2))

# Core processing chain
processed_signal = [int(x) for x in adjusted_readings]  # Convert to discrete levels
signal_energy = sum(x**2 for x in processed_signal) // len(processed_signal)

# Apply sequence analyzer
sequence_metric = analyze_sequence(processed_signal)

trend_indicator = calculate_modular_trend(processed_signal)

# State tracker for system health (partially relevant)
health_counters = {
    'stable': 0,
    'fluctuating': 0,
    'critical': 0
}
for val in processed_signal:
    if val > 7:
        health_counters['critical'] += 1
    elif val > 4:
        health_counters['fluctuating'] += 1
    else:
        health_counters['stable'] += 1

# Final performance calculation
baseline = 100
adjustment_factor = trend_indicator * 3
penalty = health_counters['critical'] * 5

final_score = baseline + int(sequence_metric) + adjustment_factor - penalty
print(f"Result: {final_score}")