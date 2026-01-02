from collections import defaultdict

# Simulate sensor readings with noise and validity flags
def generate_sensor_data():
    raw_data = [105, 98, 112, None, 103, 97, 108, 115, None, 100]
    valid_flags = [True, True, True, False, True, True, True, True, False, True]
    timestamps = [1623456780 + i*60 for i in range(10)]
    
    # Misleading transformation (not used later)
    adjusted_data = [x * 1.02 for x in raw_data if x is not None]
    outlier_threshold = 110
    temp_stats = {
        'count': len(raw_data),
        'non_null_count': len([x for x in raw_data if x is not None]),
        'outliers': [x for x in raw_data if x is not None and x > outlier_threshold]
    }
    
    return list(zip(timestamps, raw_data, valid_flags))

# Process data with filtering and weighting
def filter_and_weight(data):
    filtered_readings = []
    null_count = 0
    total_delay = 0
    
    for i, (ts, val, valid) in enumerate(data):
        if val is None or not valid:
            null_count += 1
            continue
            
        # Simulated time-based adjustment (unused red herring)
        if i > 0:
            prev_ts = data[i-1][0]
            delay = ts - prev_ts
            total_delay += delay

        # Actual relevant transformation
        if val < 100:
            adjusted_val = val * 1.1
        elif val > 110:
            adjusted_val = val * 0.95
        else:
            adjusted_val = val
            
        filtered_readings.append(adjusted_val)
    
    # Dead code path (never executed due to logic above)
    if null_count > 10:
        fallback = sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0
        filtered_readings.append(fallback)

    return filtered_readings

# Aggregation with dictionary-based weight mapping
def calculate_final_score(readings, weights_dict):
    category_map = defaultdict(list)
    
    # Categorize readings (some arbitrary thresholds)
    for v in readings:
        if v < 100:
            category_map['low'].append(v)
        elif v < 108:
            category_map['medium'].append(v)
        else:
            category_map['high'].append(v)
    
    # Unused statistical summary (distractor)
    summary_stats = {}
    for cat in ['low', 'medium', 'high']:
        if category_map[cat]:
            count = len(category_map[cat])
            avg = sum(category_map[cat]) / count
            variance = sum((x - avg) ** 2 for x in category_map[cat]) / count
            summary_stats[cat] = {'avg': avg, 'variance': variance, 'count': count}
    
    # Relevant scoring logic
    total_weighted = 0.0
    total_weight = 0.0
    
    for category, weight in weights_dict.items():
        if category_map[category]:
            cat_avg = sum(category_map[category]) / len(category_map[category])
            total_weighted += cat_avg * weight
            total_weight += weight
    
    return total_weighted / total_weight if total_weight else 0

# Main execution flow
data = generate_sensor_data()
processed = filter_and_weight(data)
weights = {'low': 0.3, 'medium': 0.4, 'high': 0.3}
final_score = calculate_final_score(processed, weights)
print(f"Result: {final_score}")