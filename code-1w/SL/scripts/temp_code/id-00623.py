from collections import defaultdict, Counter

# Simulate a data processing pipeline for sensor network (excluding actual sensor logic)

def normalize_readings(readings):
    total = sum(readings)
    if total == 0:
        return [0] * len(readings)
    return [round(x / total, 4) for x in readings]

def filter_outliers(values, threshold=2.5):
    avg = sum(values) / len(values)
    dev = [abs(v - avg) for v in values]
    max_dev = max(dev) if dev else 1
    # Normalize deviations
    norm_dev = [d / max_dev for d in dev] if max_dev > 0 else [0]*len(dev)
    return [v for v, n in zip(values, norm_dev) if n <= threshold]

def calculate_efficiency(data):
    if not data:
        return 0
    base_efficiency = 100.0
    penalty = 0
    count_entries = len(data)
    
    # Track category frequency using defaultdict
    freq_map = defaultdict(int)
    for item in data:
        freq_map[item['category']] += 1
    
    # Apply penalties based on distribution imbalance
    frequencies = list(freq_map.values())
    if frequencies:
        max_freq = max(frequencies)
        min_freq = min(frequencies)
        if min_freq > 0:
            imbalance = max_freq / min_freq
            penalty += imbalance * 1.5
    
    # Dummy transformation: case conversion for string consistency (not affecting result)
    categories_upper = [k.upper() for k in freq_map.keys()]
    categories_lower = [k.lower() for k in categories_upper]  # Redundant
    _ = [c.capitalize() for c in categories_lower]  # Dead code
    
    # Additional distraction: counting all entries regardless of use
    counter_summary = Counter([item['status'] for item in data])
    inactive_count = counter_summary.get('inactive', 0)
    active_count = counter_summary.get('active', 0)
    status_ratio = active_count / (inactive_count + 1)  # Not directly used
    
    # Efficiency degradation over volume
    volume_penalty = 0
    if count_entries > 50:
        volume_penalty = (count_entries - 50) * 0.2
    
    final_efficiency = base_efficiency - penalty - volume_penalty
    
    # Artificial clamp and rounding
    final_efficiency = max(10.0, round(final_efficiency, 3))
    
    return final_efficiency

# Simulated pre-processed dataset
raw_input_data = [
    {'value': 23.5, 'category': 'thermal', 'status': 'active'},
    {'value': 19.1, 'category': 'thermal', 'status': 'active'},
    {'value': 45.0, 'category': 'pressure', 'status': 'inactive'},
    {'value': 38.7, 'category': 'flow', 'status': 'active'},
    {'value': 41.2, 'category': 'flow', 'status': 'active'},
    {'value': 37.8, 'category': 'flow', 'status': 'active'},
    {'value': 29.3, 'category': 'thermal', 'status': 'active'},
    {'value': 52.6, 'category': 'pressure', 'status': 'active'},
    {'value': 31.0, 'category': 'thermal', 'status': 'inactive'},
    {'value': 34.8, 'category': 'flow', 'status': 'active'},
    {'value': 27.9, 'category': 'thermal', 'status': 'active'},
    {'value': 40.1, 'category': 'pressure', 'status': 'inactive'}
]

# Preprocessing steps with distractions
sum_values = sum(item['value'] for item in raw_input_data)
dummy_avg = sum_values / len(raw_input_data)
scaled_values = [x * 1.05 for x in [item['value'] for item in raw_input_data]]
normalized_readings = normalize_readings(scaled_values)
filtered_readings = filter_outliers([item['value'] for item in raw_input_data], threshold=2.0)

# Create processed data structure
processed_data = []
for reading in raw_input_data:
    entry = {
        'category': reading['category'],
        'status': reading['status']
    }
    # Some dummy derived fields
    if reading['value'] > 35:
        entry['class'] = 'high'
    elif reading['value'] > 25:
        entry['class'] = 'medium'
    else:
        entry['class'] = 'low'
    processed_data.append(entry)

# Add extra irrelevant entries to confuse analysis
for i in range(40):
    processed_data.append({
        'category': 'debug',
        'status': 'inactive',
        'class': 'low'
    })

# Key execution point
efficiency_score = calculate_efficiency(processed_data)

# Print result
print(f"Result: {efficiency_score}")