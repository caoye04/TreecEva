from itertools import compress, cycle

def analyze_sensor_stream(raw_readings, config_profile):
    # Irrelevant pre-processing: normalization (not used later)
    normalized = [round(x * 0.98 + 0.5, 3) for x in raw_readings]
    baseline_shift = sum(normalized[::3]) / len(normalized[::3])

    # Distractor: unused transformation
    inverted_signal = [1.0 / (1 + abs(x)) for x in raw_readings if x != 0]
    decay_factor = 0.87
    smoothed_inverted = []
    acc = 0.0
    for val in inverted_signal:
        acc = acc * decay_factor + val
        smoothed_inverted.append(acc)

    # Actual relevant path begins: filter valid readings
    quality_flags = [x > 50 and x < 950 for x in raw_readings]
    filtered_data = list(compress(raw_readings, quality_flags))

    # Misleading intermediate calculation (dead end)
    peak_magnitude = max(filtered_data) - min(filtered_data)
    fluctuation_index = 0
    for i in range(1, len(filtered_data)):
        if filtered_data[i] > filtered_data[i-1]:
            fluctuation_index += 1

    # Create threshold map using zip and enumerate (key python idiom)
    categories = ['temp', 'pressure', 'flow', 'humidity']
    base_thresholds = [75, 88, 200, 60]
    adjustments = [5, -2, 15, 8]
    threshold_map = dict(zip(categories, [b + a for b, a in zip(base_thresholds, adjustments)]))

    # Unused recursive helper (red herring)
    def calculate_depth(index, limit):
        if index >= limit:
            return 0
        return index + calculate_depth(index + 2, limit)

    # Real logic: count how many exceed dynamic thresholds
    temp_count = sum(1 for x in filtered_data if x > threshold_map['temp'])
    pressure_count = sum(1 for x in filtered_data if x > threshold_map['pressure'])

    # Destructuring assignment (tuple unpacking)
    primary_count, secondary_count = temp_count, pressure_count

    # Complex conditional with short-circuit evaluation
    if primary_count > 10 and (secondary_count > 5 or True):  # 'or True' makes second part irrelevant
        adjustment_phase = 1
    else:
        adjustment_phase = -1

    # Key function call that computes answer
    final_diagnostic = process_readings(filtered_data, threshold_map)
    return final_diagnostic

def process_readings(data, thresholds):
    # Use enumerate to track position-based logic
    indexed_scores = []
    for idx, value in enumerate(data):
        score = 0
        if value > thresholds['temp']:
            score += idx % 4  # depends on position
        if value > thresholds['flow']:
            score += 2
        if value < thresholds['humidity']:
            score -= 1
        indexed_scores.append(score)
    
    # Apply cycle for periodic weighting (itertools usage)
    weights = [w for w, _ in zip(cycle([1, -1, 2]), range(len(indexed_scores)))]
    weighted_sum = sum(s * w for s, w in zip(indexed_scores, weights))
    
    # Final transformation
    result = abs(weighted_sum) * 3 - 17
    return result

# Main execution
sensor_inputs = [45, 82, 901, 76, 203, 59, 88, 201, 61, 77, 205, 63, 74, 198, 58]
config = {'mode': 'diagnostic', 'version': 2}

# Trigger the analysis
final_diagnostic = analyze_sensor_stream(sensor_inputs, config)
print(f"Result: {final_diagnostic}")