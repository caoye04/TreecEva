from collections import defaultdict

# Simulate sensor pattern analysis with noise filtering and state tracking
def analyze_patterns(log_data, sensitivity):
    count_map = defaultdict(int)
    temporal_weights = [0.8, 1.2, 0.9, 1.1]
    noise_floor = 0.05
    total_energy = 0.0
    spike_count = 0

    for idx, reading in enumerate(log_data):
        base_value = abs(reading)
        weight = temporal_weights[idx % len(temporal_weights)]
        adjusted = base_value * weight

        if adjusted > sensitivity + noise_floor:
            spike_count += 1
            count_map['spike'] += 1
        elif adjusted > noise_floor:
            count_map['baseline'] += 1
        else:
            count_map['noise'] += 1  # Below detection threshold

        total_energy += adjusted ** 2

    # Irrelevant diagnostics (distractor)
    diagnostic_stats = {
        'peak': max(log_data, default=0),
        'stdev': sum((x - sum(log_data)/len(log_data))**2 for x in log_data)/len(log_data) if log_data else 0,
        'median_approx': sorted(log_data)[len(log_data)//2] if log_data else 0
    }

    # Secondary processing path with partial overlap
    filtered_readings = [r for r in log_data if abs(r) > 0.1]
    smoothed = 0
    for i in range(1, len(filtered_readings)):
        smoothed += abs(filtered_readings[i] - filtered_readings[i-1])

    # Decision logic based on pattern density
    duration_factor = len(log_data) / 100.0 if log_data else 0
    pattern_density = count_map['spike'] / len(log_data) if log_data else 0

    # Main scoring logic
    raw_score = (spike_count * 7) + int(total_energy // 10)
    penalty = 0
    if count_map['noise'] > count_map['baseline']:
        penalty += 15
    if pattern_density < 0.25:
        penalty += 10

    final_score = raw_score - penalty

    # Dead code branch (distractor)
    if False:
        backup_system = {'status': 'inactive', 'score_override': -999}
        final_score = backup_system['score_override']

    return final_score

# Simulated input data (deterministic)
sensor_stream = [
    -0.3, 0.7, 0.12, -1.4, 0.08, 0.95, -0.6, 1.8, 0.03, -0.25,
    1.1, -0.8, 0.44, 2.1, -1.3, 0.5, 0.99, -0.77, 1.05, 0.01
]

threshold = 0.5
final_score = analyze_patterns(sensor_stream, threshold)
print(f"Result: {final_score}")