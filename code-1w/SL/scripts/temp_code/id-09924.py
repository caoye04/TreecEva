def transform_signal(raw_values, factor):
    """Apply non-linear transformation to sensor signal (distractor function)"""
    return [round((x ** 0.5) * factor + 2.5, 3) for x in raw_values if x > 0]


def validate_checksum(entry):
    """Validate data entry checksum (dead code path)"""
    total = 0
    for c in str(entry):
        if c.isdigit():
            total += int(c)
    return total % 7 == 0

# Simulated sensor readings (some irrelevant)
sensor_a_readings = [16, 25, 36, 49, 64]
sensor_b_readings = [10, 20, 30, 40, 50]
sensor_c_readings = [9, 18, 27, 36, 45]  # Unused later

# Transform signals using distractor function
transformed_a = transform_signal(sensor_a_readings, 1.7)
transformed_b = transform_signal(sensor_b_readings, 1.3)

# Mapping of device IDs to thresholds (critical structure)
threshold_map = {
    'DVC-X1': 8.5,
    'DVC-Y2': 10.2,
    'DVC-Z3': 9.8
}

# Device statuses (mixed relevant and irrelevant)
device_status = {
    'DVC-X1': 'active',
    'DVC-Y2': 'standby',
    'DVC-Z3': 'active',
    'DVC-W4': 'inactive'  # Not in threshold_map, irrelevant
}

# Raw processing pipeline
raw_data_stream = [
    {'device': 'DVC-X1', 'values': [4, 9, 16]},
    {'device': 'DVC-Y2', 'values': [25, 36]},
    {'device': 'DVC-Z3', 'values': [49, 64, 81]}
]

# Intermediate aggregation (some steps are distractions)
aggregated_metrics = {}
for entry in raw_data_stream:
    dev_id = entry['device']
    squares = [x**2 for x in entry['values'] if x % 3 != 0]  # Filter logic
    logs = [round(__import__('math').log(x), 3) for x in entry['values'] if x > 1]
    aggregated_metrics[dev_id] = {
        'sum_squares': sum(squares),
        'log_series': logs,
        'count': len(logs)
    }

# Apply filtering based on status (partially relevant)
active_devices = {k: v for k, v in aggregated_metrics.items() if device_status.get(k) == 'active'}

# Further processing with string operations (distractor layer)
diagnostic_tags = set()
for dev_id, metrics in aggregated_metrics.items():
    tag = f"{dev_id[-2:].lower()}_{len(metrics['log_series'])}"
    diagnostic_tags.add(tag)

# Real processing begins: compute mean values per device
processed_data = []
for dev_id, metrics in active_devices.items():
    base_value = metrics['sum_squares'] / (metrics['count'] + 1)
    processed_data.append({'id': dev_id, 'value': round(base_value, 3)})

# Add synthetic entry for completeness (distractor)
processed_data.append({'id': 'DVC-W4', 'value': 7.1})  # Will be filtered later

# Core analysis function with recursion
def recursive_weight(index, weights):
    if index <= 0:
        return 0.5
    return weights[index % 3] * recursive_weight(index - 1, weights) + 0.1

# Analyze readings against thresholds
def analyze_readings(data_entries, limits):
    weights = [0.8, 0.9, 1.1]
    score = 0.0
    
    for i, entry in enumerate(data_entries):
        dev_id = entry['id']
        val = entry['value']
        
        # Check if device exists in limits
        if dev_id not in limits:
            continue  # Skip invalid
            
        threshold = limits[dev_id]
        diff = abs(val - threshold)
        
        # Use recursive weighting (key logic step)
        impact = recursive_weight(i, weights)
        
        # Boolean logic with short-circuiting
        severity = (diff > 2.0) or (val < 5.0 and threshold > 10.0)
        
        # Final contribution
        if severity:
            score -= diff * impact
        else:
            score += (threshold - diff) * impact
    
    # Additional distraction: zip and enumerate on unrelated data
    labels = ['A', 'B', 'C']
    temp_pairs = list(zip(labels, transformed_a[:3]))
    extra_offset = 0
    for idx, (lbl, val) in enumerate(temp_pairs):
        if lbl in 'BD':
            extra_offset += val * 0.01  # Negligible effect
    
    # Critical answer computation
    final_score = round(score + extra_offset, 3)
    
    # Destructuring distraction
    a, b = 123, 456
    c, d = b, a  # Swap, irrelevant
    
    # Set operation red herring
event_set = {f"evt_{i}" for i in range(5)}
    debug_set = {f"dbg_{j}" for j in range(3)}
    overlap = event_set & debug_set  # Empty, useless
    
    return final_score

# Execute main analysis
final_diagnostic = analyze_readings(processed_data, threshold_map)
print(f"Target result: {final_diagnostic}")