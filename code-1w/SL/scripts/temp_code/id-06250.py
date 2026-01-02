def calculate_final_score(raw_data, limits):
    # Preprocessing: Normalize and filter data
    normalized = [round((x - min(raw_data)) / (max(raw_data) - min(raw_data)) * 100, 2) for x in raw_data]
    filtered = [val for val in normalized if val >= limits['min_thresh']]

    # Irrelevant distraction: Character analysis on fake labels
    labels = ['A', 'B', 'C', 'D', 'E']
    label_lengths = [len(l.lower().replace('a', 'x')) for l in labels]  # Distractor computation
    temp_sum = sum(label_lengths) * 0.5  # Not used later

    # Statistical calculations with enumeration
    deviations = []
    base_ref = sum(filtered) / len(filtered) if filtered else 0
    for i, val in enumerate(filtered):
        if i % 2 == 0:
            deviations.append(abs(val - base_ref) ** 0.5)
        else:
            deviations.append(abs(val - base_ref) * 0.1)  # Alternate weighting

    # Secondary distraction: zipping unrelated sequences
    indices = list(range(len(deviations)))
    paired = list(zip(indices, deviations))  # Used only for dummy aggregation
    dummy_total = sum([p[1] for p in paired if p[0] % 3 == 0])  # Dead-end path

    # Core logic: weighted score based on threshold zones
    zone_weights = []
    for v in filtered:
        if v < limits['mid_thresh']:
            zone_weights.append(1.0)
        elif v < limits['high_thresh']:
            zone_weights.append(1.8)
        else:
            zone_weights.append(2.5)

    weighted_sum = sum(f * w for f, w in zip(filtered, zone_weights))
    penalty = len([d for d in deviations if d > 10]) * 1.5  # Small adjustment

    final_score = round(weighted_sum - penalty, 2)
    return final_score

# Main execution
sensor_readings = [12, 45, 67, 89, 23, 78, 91]
cutoffs = {
    'min_thresh': 20,
    'mid_thresh': 50,
    'high_thresh': 75
}

intermediate_avg = sum(sensor_readings) / len(sensor_readings)  # Unused tracking
scaling_factor = max(sensor_readings) / 100  # Red herring

final_score = calculate_final_score(sensor_readings, cutoffs)
print(f"Result: {final_score}")