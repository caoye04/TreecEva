def analyze_metrics(raw_values):
    # Irrelevant transformation
    temp_offset = sum(raw_values) * 0.1
    adjusted = [x + temp_offset for x in raw_values]

    # Distractor computation
    outlier_count = 0
    for val in adjusted:
        if val > 100:
            outlier_count += 1

    # Actual relevant logic
    valid_data = [x for x in adjusted if x <= 100]
    avg = sum(valid_data) / len(valid_data) if valid_data else 0
    return {'average': avg, 'count': len(valid_data)}


def preprocess_input(entries):
    # String manipulation as red herring
    key_names = [k.upper().replace('_', '') for k in entries.keys()]
    sorted_keys = sorted(key_names)

    # Real processing
    values = list(entries.values())
    scaled = [v * 2 for v in values]
    return scaled

# Misleading data structure
auxiliary_map = {
    'temp_cap': 45,
    'debug_flag': True,
    'buffer': [0] * 5
}

# Input data
sensor_readings = {
    'sensor_a': 12,
    'sensor_b': 18,
    'sensor_c': 24,
    'sensor_d': 36
}

# Processing steps with mixed relevance
processed_values = preprocess_input(sensor_readings)

# Distractor: unused statistical calculation
variance_proxy = 0
if len(processed_values) > 1:
    mean_val = sum(processed_values) / len(processed_values)
    variance_proxy = sum((x - mean_val) ** 2 for x in processed_values) / len(processed_values)

# Core analysis (uses only part of prior work)
data_summary = analyze_metrics(processed_values)

# Red herring: dead code path
if auxiliary_map['debug_flag']:
    pass  # Simulated diagnostics

# Key computation involving dictionary and logical condition
base_score = data_summary['average'] * data_summary['count']
bonus = 10 if data_summary['count'] >= 3 else 0
penalty = 5 if data_summary['average'] < 50 else 0

# Final score depends only on specific derived values
final_score = base_score + bonus - penalty

# Output required format
print(f"Result: {final_score}")