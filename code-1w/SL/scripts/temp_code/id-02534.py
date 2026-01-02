from collections import defaultdict, Counter

# Simulate sensor data with noise and redundancy
def preprocess_data(raw_samples):
    processed = []
    noise_offset = 0.1
    for sample in raw_samples:
        if sample['type'] == 'temp':
            corrected = sample['value'] + noise_offset
            processed.append(('temperature', corrected))
        elif sample['type'] == 'pressure':
            adjusted = sample['value'] * 0.98
            processed.append(('pressure', adjusted))
    return processed

# Analyze frequency of readings and apply weighting
def calculate_stability_metrics(entries):
    freq = Counter()
    values_by_type = defaultdict(list)
    
    for entry_type, value in entries:
        freq[entry_type] += 1
        values_by_type[entry_type].append(value)
    
    averages = {}
    for t in values_by_type:
        averages[t] = sum(values_by_type[t]) / len(values_by_type[t])
    
    # Dummy metric - not used but adds distraction
    total_entries = sum(freq.values())
    dummy_metric = total_entries * 0.5 if total_entries > 10 else 0
    
    return averages, freq

# Core scoring logic
def calculate_final_score(sensor_data, importance_weights):
    base_scores = {}
    for key, avg_val in sensor_data.items():
        if key == 'temperature':
            # Normalize to baseline (25°C)
            deviation = abs(avg_val - 25.0)
            temp_score = 100 - (deviation * 2)
            base_scores['temp_norm'] = max(temp_score, 0)
        elif key == 'pressure':
            # Pressure should be around 101.3 kPa
            deviation = abs(avg_val - 101.3)
            pressure_score = 90 - (deviation * 0.5)
            base_scores['press_adj'] = max(pressure_score, 0)
    
    # Apply bitwise adjustment based on weight flags
    combined_flag = importance_weights['critical'] & importance_weights['active']
    modifier = 1.1 if combined_flag else 0.9
    
    # Final aggregation
    raw_total = 0
    for score in base_scores.values():
        raw_total += score
    
    final_score = raw_total * modifier
    
    # Irrelevant transformations below (distractors)
    squared_error = (final_score - 180) ** 2
    normalized_err = squared_error / 1000.0
    diagnostic_code = int(normalized_err) ^ 42
    
    return final_score

# Main execution
if __name__ == "__main__":
    # Raw input data from sensors
    raw_input = [
        {'type': 'temp', 'value': 24.8},
        {'type': 'temp', 'value': 25.1},
        {'type': 'temp', 'value': 24.9},
        {'type': 'pressure', 'value': 102.0},
        {'type': 'pressure', 'value': 100.8},
        {'type': 'pressure', 'value': 101.5}
    ]

    # Preprocess the raw data
    cleaned_data = preprocess_data(raw_input)

    # Extract stability characteristics
    avg_readings, count_freq = calculate_stability_metrics(cleaned_data)

    # Define weight configuration
    weights = {
        'critical': 0b1101,
        'active': 0b1011,
        'priority': 0b0110
    }

    # Compute final system score
    final_score = calculate_final_score(avg_readings, weights)

    # Output result
    print(f"Result: {final_score}")