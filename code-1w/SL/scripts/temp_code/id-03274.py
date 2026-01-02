from collections import defaultdict, Counter

# Simulate sensor data with noise and metadata
def generate_sensor_data():
    raw_readings = [15, 22, 8, 41, 19, 33, 27, 12]
    timestamps = [100, 101, 102, 104, 106, 108, 110, 111]
    statuses = ['OK', 'OK', 'ERROR', 'OK', 'WARNING', 'OK', 'OK', 'ERROR']
    
    data_bundle = []
    for i in range(len(raw_readings)):
        data_bundle.append({
            'value': raw_readings[i],
            'time': timestamps[i],
            'status': statuses[i]
        })
    return data_bundle

# Auxiliary function to compute moving average (not used in final result)
def moving_average(values, window=2):
    avgs = []
    for i in range(len(values) - window + 1):
        avgs.append(sum(values[i:i+window]) / window)
    return avgs

# Core logic for scoring valid data segments
def calculate_validity_score(entries):
    score = 0
    penalty_adjustment = 0.0
    
    # Track status distribution (distractor: not directly used)
    status_count = defaultdict(int)
    value_history = []
    
    for entry in entries:
        status_count[entry['status']] += 1
        value_history.append(entry['value'])
        
        if entry['status'] == 'OK':
            score += entry['value'] * 1.1
        elif entry['status'] == 'WARNING':
            score += entry['value'] * 0.5
        else:
            score -= entry['value'] * 0.3
    
    # Dead code path - never executed due to data
    if 'CRITICAL' in status_count:
        penalty_adjustment = -100
    
    # Unused intermediate calculation
    avg_value = sum(value_history) / len(value_history) if value_history else 0
    variance_proxy = sum((v - avg_value) ** 2 for v in value_history) / len(value_history) if value_history else 0
    
    return int(score)

# Determine outlier indices based on threshold (irrelevant computation)
def find_outliers(values, t=25):
    outliers = []
    for i, v in enumerate(values):
        if v > t:
            outliers.append(i)
    return outliers

# Main processing function
def calculate_final_score(data_map, threshold):
    total_base = 0
    adjustment_factor = 0
    debug_log = []
    
    # Build category map (distractor structure)
    category_map = defaultdict(list)
    for item in data_map:
        cat_key = 'high' if item['value'] > threshold else 'low'
        category_map[cat_key].append(item)
    
    # Process only 'high'-threshold values for score
    high_group = category_map['high']
    low_group = category_map['low']  # computed but unused
    
    # Accumulate base from high group
    for item in high_group:
        total_base += item['value']

    # Secondary scoring using validity logic
    validity_bonus = calculate_validity_score(data_map)
    
    # Red herring: character frequency analysis on status codes
    all_statuses = ''.join(item['status'] for item in data_map)
    char_freq = Counter(all_statuses)
    rare_chars = [ch for ch, cnt in char_freq.items() if cnt < 2]
    adjustment_factor = len(rare_chars) * 2  # looks relevant but isn't
    
    # Final composition
    temp_result = total_base + validity_bonus
    scaling_shift = len(high_group) - len(low_group)  # neutral effect
    final_component = temp_result + scaling_shift + adjustment_factor
    
    # Key assignment point
    final_score = final_component * 2 // 3  # ensures integer result
    
    # Spurious post-calculation
    normalized = final_score / (sum(char_freq.values()) or 1)
    debug_log.append(f'Final normalized: {normalized:.3f}')
    
    return final_score

# Setup and execution
data_entries = generate_sensor_data()
data_map = {i: data_entries[i] for i in range(len(data_entries))}
threshold = 20

# Execute main logic
final_score = calculate_final_score(data_map, threshold)
print(f"Result: {final_score}")