def analyze_readings(sensor_readings):
    filtered_readings = [x for x in sensor_readings if x > 25 and x < 95]
    offset = 3
    adjusted_readings = [x + offset for x in filtered_readings]
    outlier_count = sum(1 for x in adjusted_readings if x < 30 or x > 90)
    valid_readings = [x for x in adjusted_readings if 30 <= x <= 90]
    
    # Irrelevant transformations
    temp_stats = {
        'max_val': max(valid_readings, default=0),
        'min_val': min(valid_readings, default=0),
        'range_val': max(valid_readings, default=0) - min(valid_readings, default=0)
    }
    
    bucket_counts = {i: 0 for i in range(30, 91, 10)}
    for val in valid_readings:
        bucket = (val // 10) * 10
        if bucket in bucket_counts:
            bucket_counts[bucket] += 1
    
    reading_pairs = [(a, b) for idx, a in enumerate(valid_readings) 
                      for b in valid_readings[idx+1:] if abs(a - b) < 5]
    pair_stability = len(reading_pairs) / len(valid_readings) if valid_readings else 0
    
    return {
        'readings': valid_readings,
        'outliers': outlier_count,
        'stability': pair_stability,
        'buckets': bucket_counts
    }


def calculate_efficiency(data_dict):
    base_efficiency = len(data_dict['readings'])
    penalty = data_dict['outliers'] * 2
    bonus = int(data_dict['stability'] * 10)
    efficiency = base_efficiency - penalty + bonus
    
    # Dummy intermediate calculations (distractors)
    temp_factor = 1.0
    if data_dict['buckets'][40] > 0:
        temp_factor *= 1.1
    if data_dict['buckets'][80] > 0:
        temp_factor *= 0.9
    
    adjusted_efficiency = int(efficiency * temp_factor)
    
    # Extra unused variables to increase interference
    summary_text = f"Processed {len(data_dict['readings'])} values"
    debug_info = {'version': '2.1', 'mode': 'calibration'}
    
    return adjusted_efficiency

# Main execution
raw_data = [20, 26, 27, 35, 41, 42, 43, 50, 55, 59, 60, 61, 62, 65, 70, 75, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 96]
processed_data = analyze_readings(raw_data)
efficiency_score = calculate_efficiency(processed_data)
print(f"Result: {efficiency_score}")