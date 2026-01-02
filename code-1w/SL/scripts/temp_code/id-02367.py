from collections import defaultdict

# Simulate sensor data aggregation and filtering
def preprocess_sensors(raw_readings):
    temp_data = defaultdict(list)
    for sensor_id, reading in raw_readings:
        temp_data[sensor_id].append(reading)
    
    filtered_data = {}
    for sid, readings in temp_data.items():
        avg_val = sum(readings) / len(readings)
        if avg_val > 25:
            filtered_data[sid] = round(avg_val, 2)
    return filtered_data

# Transform into categorized buckets
def categorize_temperatures(data):
    categories = {'high': [], 'moderate': []}
    debug_stats = {'processed': 0, 'discarded': 0}  # Distractor: not used later
    
    for k, v in data.items():
        if v > 30:
            categories['high'].append(k)
        elif v > 25:
            categories['moderate'].append(k)
    
    # Spurious computation - irrelevant to final result
    total_keys = len(data)
    if total_keys > 0:
        dummy_metric = (len(categories['high']) * 100) // total_keys
    
    return categories

# Core scoring logic
def compute_stability_index(category_map, raw_count):
    high_count = len(category_map['high'])
    mod_count = len(category_map['moderate'])
    index = (high_count * 1.5) + (mod_count * 0.8)
    adjustment = raw_count - (high_count + mod_count)  # Unused path
    if adjustment > 5:
        index *= 1.1
    return index

# Final score calculation
def calculate_final_score(dataset):
    size_factor = len(dataset) * 2
    base_index = compute_stability_index(dataset, len(dataset))
    bonus = 0
    
    # Conditional bonus based on distribution
    if 'high' in dataset and len(dataset['high']) >= 2:
        bonus = 10
    
    # Red herring: complex-looking but unused formula
    fallback_score = 0
    for val in dataset.get('moderate', []):
        fallback_score += val % 7
    
    result = int(size_factor + base_index + bonus)
    return result

# Main execution
if __name__ == '__main__':
    sensor_inputs = [
        ('S1', 32), ('S1', 33), ('S1', 24),
        ('S2', 28), ('S2', 29),
        ('S3', 35), ('S3', 36),
        ('S4', 22), ('S4', 23),
        ('S5', 31), ('S5', 30)
    ]

    intermediate_result = preprocess_sensors(sensor_inputs)
    processed_data = categorize_temperatures(intermediate_result)
    
    # Irrelevant transformation - distractor
    inverted_map = {v: k for k, v in enumerate(processed_data['high'])}
    
    final_score = calculate_final_score(processed_data)
    print(f"Target result: {final_score}")