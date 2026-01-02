def analyze_temperatures(temps):
    above_freezing = [t for t in temps if t > 0]
    below_freezing = [t for t in temps if t <= 0]
    avg_temp = sum(temps) / len(temps) if temps else 0
    temp_range = max(temps) - min(temps) if temps else 0
    
    # Distractor: unused statistical measures
    variance = sum((t - avg_temp) ** 2 for t in temps) / len(temps) if temps else 0
    std_dev = variance ** 0.5
    median_temp = sorted(temps)[len(temps)//2] if temps else 0

    return {'avg': avg_temp, 'range': temp_range, 'count': len(above_freezing)}


def validate_readings(readings):
    valid = []
    invalid_count = 0
    for i, r in enumerate(readings):
        if isinstance(r, (int, float)) and -100 <= r <= 100:
            valid.append(r)
        else:
            invalid_count += 1
    
    # Distractor: extra logging not used later
    log_entries = [f'Reading {i}: {r}' for i, r in enumerate(readings[:3])]
    total_skipped = len(readings) - len(valid)
    
    return valid


def calculate_final_score(data):
    base_score = 0
    for key, values in data.items():
        if key.startswith('sensor'):
            base_score += sum(v * 0.1 for v in values if v > 5)
    
    adjustment = len(data.get('sensor_offsets', [])) * -2
    final_score = int(base_score) + adjustment
    
    # Critical point
    return final_score

# Main execution
raw_data = [-5, 12, 45, 67, -23, 0, 15, 99]
labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug']

zipped_info = list(zip(raw_data, labels))
filtered_data = [temp for temp, _ in zipped_info if 'u' in _]  # Months with 'u': Jun, Jul, Aug

validated_temps = validate_readings(filtered_data + [None, -200])
analysis_result = analyze_temperatures(validated_temps)

# Construct processed data with multiple sensor entries
processed_data = {
    'sensor_a': [10, 15, 20, 25],
    'sensor_b': [8, 18, 6, 30, 50],
    'sensor_c': [12, -5, 44],
    'sensor_offsets': [0.5, -0.3, 0.7],
    'metadata': analysis_result
}

# Extra distraction: unused transformation
transformed = {k: [x**0.5 for x in v] if isinstance(v, list) and all(isinstance(x, (int,float)) for x in v) else v 
               for k, v in processed_data.items()}
square_root_influence = sum(len(v) for v in transformed.values() if isinstance(v, list)) * 0.01

final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")