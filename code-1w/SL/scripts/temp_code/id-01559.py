def filter_anomalies(data, limit):
    # Remove readings below threshold (considered noise)
    filtered = [x for x in data if x >= limit]
    normalization_factor = sum(filtered) / len(filtered) if filtered else 0
    scaled = [x / normalization_factor for x in filtered]  # Normalize, not used later
    return set(filtered)  # Return as set to enable set operations


def calculate_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq_map.values():
        prob = count / total
        entropy -= prob * log2(prob)
    return round(entropy, 4)


def analyze_readings(valid_set, base):
    # Convert set to sorted list for processing
    readings = sorted(valid_set)
    
    # Irrelevant computation: simulate calibration drift
    drift_compensation = 0
    for i in range(len(readings)):
        if readings[i] > base * 1.5:
            drift_compensation += 0.1
        elif readings[i] < base * 0.5:
            drift_compensation -= 0.05
    
    # Actual logic: count significant deviations
    deviation_count = 0
    running_total = 0
    for val in readings:
        if val > base * 1.2:
            deviation_count += 1
        if val < base * 0.8:
            deviation_count -= 1
        running_total += val
    
    # Secondary distraction: simulate checksum
    temp_checksum = 0
    for i, v in enumerate(readings):
        temp_checksum ^= (v * (i + 1)) % 100
    
    # Core result: weighted diagnostic score
    stability_index = len(readings) * 2
    fluctuation_penalty = abs(deviation_count) * 3
    final_diagnostic = stability_index - fluctuation_penalty + (running_total // 100)
    
    return final_diagnostic

# Main execution
sensor_data = [105, 90, 120, 85, 130, 70, 110, 115, 60, 125, 100]
baseline = 100
threshold = 75

# Preprocessing side calculation (distractor)
avg_before = sum(sensor_data) / len(sensor_data)
high_readings = [x for x in sensor_data if x > 110]
dominant_set = {x for x in sensor_data if x > 90}  # Set comprehension

# Key execution point
final_diagnostic = analyze_readings(filter_anomalies(sensor_data, threshold), baseline)

print(f"Result: {final_diagnostic}")