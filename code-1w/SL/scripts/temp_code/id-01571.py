def analyze_system_performance(input_data):
    # Irrelevant transformation: case conversion and string manipulation
    processed_labels = [label.upper().replace('_', ' ') for label in input_data.get('labels', [])]
    normalized_data = []

    for val in input_data.get('values', []):
        if val < 0:
            normalized_data.append(abs(val) * 0.9)
        elif val > 100:
            normalized_data.append(100)
        else:
            normalized_data.append(val)

    # Distractor: dead code path (never executed due to fixed condition)
    system_flags = {'overload': False, 'degraded': False}
    if len(processed_labels) > 1000:  # Impossible in this context
        system_flags['overload'] = True

    # Relevant: compute efficiency factor using arithmetic and rounding
    base_score = sum(normalized_data) / len(normalized_data) if normalized_data else 0
    adjustment_factor = round(base_score * 0.12, 2)
    efficiency_index = int((base_score + adjustment_factor) // 1)

    # Distractor: unused list comprehension with bit shifting (no effect on result)
    diagnostic_codes = [efficiency_index << 1 ^ i for i in range(3) if i % 2 == 0]

    # Relevant: generate efficiency log with filtered thresholds
    efficiency_log = []
    for i in range(1, 6):
        threshold = (efficiency_index + i * 2) // 3
        if threshold % 2 == 0:
            efficiency_log.append(threshold * 1.5)
        else:
            efficiency_log.append(threshold * 0.75)

    # Distractor: irrelevant dictionary construction
    status_report = {
        'timestamp': '2024-01-01T00:00:00Z',
        'version': '3.7.1',
        'metrics': {k: len(v) if isinstance(v, list) else v for k, v in input_data.items()}
    }

    return efficiency_log


def calculate_thermal_rating(log_entries):
    # Complex data transformation with integer division and conditional logic
    total_weight = 0
    scaling_factor = 2.5

    for idx, entry in enumerate(log_entries):
        if idx % 2 == 0:
            # Even indices use ceiling-like behavior via negation and floor
            adjusted = -(-int(entry) // 1)  # Simulate ceiling
            total_weight += (adjusted * scaling_factor) // 2
        else:
            # Odd indices use truncating division
            truncated = int(entry)
            total_weight -= (truncated // 3) * idx

    # Apply final correction using sum of digits in total_weight (if positive)
    temp_sum = 0
    remainder_check = abs(total_weight)
    while remainder_check > 0:
        temp_sum += remainder_check % 10
        remainder_check //= 10

    if total_weight > 0:
        total_weight += temp_sum * 2
    else:
        total_weight -= temp_sum

    return total_weight

# Main execution block
input_payload = {
    'labels': ['sensor_A', 'sensor_B', 'sensor_C'],
    'values': [85, 92, 78, 63, 95, 44, 88]
}

# Execute analysis
log_output = analyze_system_performance(input_payload)

# Key statement: calculate thermal capacity from efficiency log
thermal_capacity = calculate_thermal_rating(log_output)

# Output result as required
print(f"Result: {thermal_capacity}")