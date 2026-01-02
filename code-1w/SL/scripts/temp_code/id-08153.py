from collections import defaultdict, Counter

# Simulate sensor data aggregation and analysis for a smart irrigation system
def analyze_irrigation_efficiency(sensor_readings, calibration_factor):
    raw_stats = defaultdict(int)
    quality_flags = []
    total_volume = 0.0
    valid_entries = 0

    # Preprocess: filter and classify readings
    for entry in sensor_readings:
        zone_id = entry['zone']
        moisture = entry['moisture']
        pressure = entry['pressure']
        timestamp = entry['time']

        if moisture < 0 or pressure < 0:
            quality_flags.append('INVALID')
            continue

        if moisture > 100:
            moisture = 100
        if pressure > 50:
            adjusted_pressure = 50 * calibration_factor
        else:
            adjusted_pressure = pressure * calibration_factor

        raw_stats[zone_id] += moisture * adjusted_pressure
        total_volume += adjusted_pressure
        valid_entries += 1

        # Distractor computation: tracking timestamps but not used later
        day_period = 'morning' if 6 <= timestamp < 12 else 'afternoon' if 12 <= timestamp < 18 else 'evening'
        _ = f'Data from {day_period}'  # Dead code path

    # Secondary distractor: unused statistical analysis
    if valid_entries > 0:
        avg_volume = total_volume / valid_entries
        volume_deviation = abs(avg_volume - 25.0)
    else:
        avg_volume = 0
        volume_deviation = 0

    # Simulate data processing pipeline
    processed_data = []
    zone_contributions = Counter()

    for zone, cumulative_score in raw_stats.items():
        normalized_score = cumulative_score / (valid_entries + 1)
        zone_contributions[zone] = round(normalized_score, 3)
        if normalized_score > 150:
            processed_data.append({'zone': zone, 'score': normalized_score, 'priority': 'HIGH'})
        elif normalized_score > 75:
            processed_data.append({'zone': zone, 'score': normalized_score, 'priority': 'MEDIUM'})
        else:
            processed_data.append({'zone': zone, 'score': normalized_score, 'priority': 'LOW'})

    # Another irrelevant metric
    high_priority_count = sum(1 for x in processed_data if x['priority'] == 'HIGH')
    priority_ratio = high_priority_count / len(processed_data) if processed_data else 0

    # Threshold determined from environmental heuristics
    threshold = 90.0 + (calibration_factor * 5)

    # Core calculation function embedded to increase nesting
    def calculate_efficiency(data, thresh):
        base_efficiency = 100.0
        penalty = 0.0
        bonus = 0.0

        for record in data:
            score = record['score']
            if score > thresh:
                bonus += 7.5
            elif score < thresh * 0.5:
                penalty += 4.2

        efficiency = base_efficiency + bonus - penalty
        return max(0, efficiency)  # Ensure non-negative

    efficiency_score = calculate_efficiency(processed_data, threshold)
    return efficiency_score

# Input data
readings = [
    {'zone': 'A1', 'moisture': 85, 'pressure': 30, 'time': 7},
    {'zone': 'A2', 'moisture': 40, 'pressure': 20, 'time': 8},
    {'zone': 'B1', 'moisture': 95, 'pressure': 45, 'time': 13},
    {'zone': 'C1', 'moisture': 30, 'pressure': 15, 'time': 14},
    {'zone': 'C2', 'moisture': 20, 'pressure': 10, 'time': 16},
    {'zone': 'A1', 'moisture': 75, 'pressure': 25, 'time': 19}
]

efficiency_result = analyze_irrigation_efficiency(readings, calibration_factor=1.1)
Result: {efficiency_result}