from collections import defaultdict, Counter
import math

# Simulated sensor data with noise and metadata
data_packet = [
    {'id': 'A7', 'readings': [1.2, 3.4, -2.1, 8.9], 'status': 'active'},
    {'id': 'B3', 'readings': [0.0, -1.1, 4.5, 3.2], 'status': 'inactive'},
    {'id': 'C9', 'readings': [2.3, 1.8, 0.5, 7.7], 'status': 'active'}
]

# Irrelevant helper function (decoy)
def calculate_efficiency(rating):
    return (rating * 1.7) + 32

# Unused transformation map
effect_map = {'A7': 0.92, 'B3': 0.87, 'C9': 1.03}

# Distractor variables
total_sensors = len(data_packet)
overall_avg = 0.0
running_stats = []

# Simulated timestamp processing (irrelevant)
current_log = "LOG_2024-06-15"
log_parts = current_log.split('_')
date_segment = log_parts[1] if len(log_parts) > 1 else ""

# Data normalization with red herring logic
def normalize_readings(raw_data):
    normalized = []
    for entry in raw_data:
        if entry['status'] != 'active':
            continue
        clean_vals = [abs(x) for x in entry['readings'] if x != 0.0]
        adjusted = [val * 0.85 for val in clean_vals]  # arbitrary scaling
        normalized.append({'id': entry['id'], 'values': adjusted})
    return normalized

# Signal filtering with misleading intermediate steps
def filter_anomalies(normalized_list):
    filtered = []
    anomaly_count = 0
    for item in normalized_list:
        mean_val = sum(item['values']) / len(item['values'])
        deviations = [(x - mean_val)**2 for x in item['values']]
        variance = sum(deviations) / len(deviations) if deviations else 0
        # Threshold check (only some pass)
        if variance < 10.0:
            item['variance'] = round(variance, 4)
            filtered.append(item)
        else:
            anomaly_count += 1
    return filtered

# Signal transformation with decoy operations
def transform_signal(filtered_data):
    transformed = []n    temp_store = defaultdict(float)
    
    for record in filtered_data:
        values = record['values']
        # Real operation: FFT-like magnitude approximation
        magnitude = sum(math.sin(x) ** 2 + math.cos(x) ** 2 for x in values)
        # Distractor: unused frequency shift
        shifted = [x * 1.05 for x in values]
        temp_store[record['id']] = sum(shifted)
        # Only magnitude matters
        transformed.append({'id': record['id'], 'mag': magnitude})
    
    # Fake checksum (never used)
    checksum = sum(len(r['values']) for r in filtered_data) * 17
    
    return transformed

# Core analysis with critical computation path
def analyze_signal(transformed_list):
    results = []
    id_contributions = Counter()
    
    for entry in transformed_list:
        raw_mag = entry['mag']
        # Key arithmetic transformation
        processed_mag = (raw_mag * 2.3) - 1.7
        
        # Conditional branching affecting final result
        if 'A' in entry['id']:
            processed_mag *= 0.9
        elif 'C' in entry['id']:
            processed_mag += 0.5
        else:
            processed_mag -= 0.2
        
        id_contributions[entry['id']] = round(processed_mag, 4)
        results.append(processed_mag)
    
    # Final aggregation - this is where the answer comes from
    base_result = sum(results)
    adjustment_factor = len(id_contributions) * 0.33
    final_score = base_result - adjustment_factor
    
    # Dead code path (misleading)
    if final_score < 0:
        final_score = abs(final_score) * 1.5
    
    # This variable is never used but looks important
    diagnostic_trace = ''.join(sorted(id_contributions.keys()))
    
    # The actual target variable
    final_diagnostic = int(round(final_score * 100))
    
    return final_diagnostic

# Execution pipeline
normalized_data = normalize_readings(data_packet)
filtered_data = filter_anomalies(normalized_data)
transformed_data = transform_signal(filtered_data)
final_diagnostic = analyze_signal(transformed_data)

print(f"Result: {final_diagnostic}")