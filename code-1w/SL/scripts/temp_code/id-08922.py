from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
def generate_noisy_sensor_data():
    raw_readings = [15, 18, 15, 22, 18, 25, 15, 22, 30, 25, 18, 22]
    timestamps = list(range(len(raw_readings)))
    return list(zip(timestamps, raw_readings))

def filter_outliers_and_aggregate(data, threshold=2):
    # Extract values and count frequency
    values = [entry[1] for entry in data]
    freq = Counter(values)
    
    # Identify outliers (values appearing less than threshold)
    filtered_values = [v for v in values if freq[v] >= threshold]
    
    # Misleading computation: average of all, not used later
    overall_avg = sum(values) / len(values) if values else 0
    temp_result = [x for x in filtered_values if x > overall_avg]  # semi-relevant filtering
    
    # Aggregate by counting occurrences above median
    if not filtered_values:
        return 0
    sorted_vals = sorted(set(filtered_values))
    median_val = sorted_vals[len(sorted_vals)//2]
    above_median_count = len([v for v in filtered_values if v > median_val])
    
    # Return a weighted score
    return (sum(filtered_values) // len(filtered_values)) + above_median_count

def calculate_final_score(data_map):
    # Data map has keys as sensor types, we only care about 'primary'
    primary_data = data_map.get('primary', [])
    backup_data = data_map.get('backup', [])  # dead code path, never used
    
    base_score = filter_outliers_and_aggregate(primary_data)
    
    # Additional distraction: secondary processing that doesn't change outcome
    secondary_stats = {}
    for val in primary_data:
        key = val[1] // 5
        secondary_stats[key] = secondary_stats.get(key, 0) + 1
    
    adjustment_factor = len(secondary_stats) % 4  # some arbitrary tweak
    
    final = base_score + adjustment_factor
    
    # Irrelevant loop: simulates logging but changes nothing
    log_entries = []
    for item in primary_data:
        if item[1] > 20:
            log_entries.append(f"High reading at t{item[0]}")
    
    return final

# Main execution
sensor_data = generate_noisy_sensor_data()

data_dict = defaultdict(list)
for ts, val in sensor_data:
    if val < 20:
        data_dict['primary'].append((ts, val))
    else:
        data_dict['primary'].append((ts, val))  # all go to primary
    data_dict['junk'].append((ts, val*2))  # red herring entries

# Key statement
final_score = calculate_final_score(data_dict)

print(f"Result: {final_score}")