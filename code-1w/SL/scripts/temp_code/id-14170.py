import math

def analyze_component(x, y):
    return (x ** 2 + y ** 2) ** 0.5

def dummy_analysis(arr):
    temp_sum = 0
    for i in range(len(arr)):
        temp_sum += arr[i] * (i + 1)
    scaling_factor = 1.5  # unused red herring
    normalized = [val / (temp_sum + 1e-8) for val in arr]
    return sum(normalized)  # dead-end computation

data_log = [
    {'id': 1, 'values': [3, 4], 'active': True, 'flags': [1, 0, 1]},
    {'id': 2, 'values': [5, 12], 'active': False, 'flags': [0, 1, 1]},
    {'id': 3, 'values': [8, 15], 'active': True, 'flags': [1, 1, 0]}
]

config = {
    'threshold': 10,
    'weight_a': 0.7,
    'weight_b': 0.3,
    'debug_mode': True,
    'max_entries': 100
}

# Irrelevant preprocessing block (distractor)
preprocessed_flags = []
for entry in data_log:
    flag_sum = sum(entry['flags'])
    if flag_sum > 1:
        preprocessed_flags.append(True)
    else:
        preprocessed_flags.append(False)

# Unused transformation function (red herring)
transform_data = lambda x: [analyze_component(v[0], v[1]) for v in x]
dummy_result = transform_data([[3,4],[5,6]])

# Decoy metric calculation (misleading intermediate)
temp_metrics = []
for record in data_log:
    magnitude = analyze_component(record['values'][0], record['values'][1])
    temp_metrics.append(magnitude if record['active'] else 0)

total_temp = sum(temp_metrics)
avg_temp = total_temp / len(temp_metrics) if temp_metrics else 0

# Real processing begins here — deeply nested and obscured
aggregated = 0
contributions = []

for item in data_log:
    if item['active']:
        raw_vals = item['values']
        base_metric = analyze_component(raw_vals[0], raw_vals[1])
        
        adjustment = 0
        if base_metric > config['threshold']:
            adjustment = config['weight_a'] * base_metric
        else:
            adjustment = config['weight_b'] * base_metric * 0.5
        
        # Nested conditional with tuple unpacking
        multiplier = 1.0
        flags = item['flags']
        for i, f in enumerate(flags):
            if f == 1:
                if i == 0:
                    multiplier *= 1.1
                elif i == 1:
                    multiplier *= 1.05
                elif i == 2:
                    # Complex conditional branch that affects final result
                    if base_metric > 10 and adjustment < 15:
                        multiplier *= 0.9
                    else:
                        multiplier *= 1.0
        
        final_component = (adjustment * multiplier)
        contributions.append(final_component)
        aggregated += final_component

# Linear search for dominant contributor (tuple used)
max_index = -1
max_value = -1
for idx, val in enumerate(contributions):
    if val > max_value:
        max_value = val
        max_index = idx

dominant_entry = (max_index, max_value) if max_index != -1 else None

# Secondary adjustment based on dominant
penalty_factor = 0.9 if dominant_entry and dominant_entry[0] == 2 else 1.0
adjusted_aggregated = aggregated * penalty_factor

# Efficiency score derived from multiple logic layers
buffer_size = 1024
overhead = buffer_size * 0.01  # irrelevant system parameter

# Core answer computation — depends on all prior logic
efficiency_score = round(adjusted_aggregated * 100) / 100

# Final output assignment (key statement)
final_output = process_metrics(data_log, config) if 'process_metrics' in globals() else efficiency_score

# Simulate missing function by assigning directly
final_output = efficiency_score

print(f"Result: {final_output}")