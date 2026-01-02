def process_performance(data, modifiers):
    base_score = 0
    penalty_adjustment = 0.0
    temp_result = []

    # Irrelevant string processing (distractor)
    status_log = "System: Performance evaluation initiated."
    log_parts = status_log.lower().split(':')
    system_status = log_parts[1].strip()

    # Real computation begins
    for key in data:
        if key.startswith('metric_'):
            base_score += data[key]

    # Apply multiplier from modifiers
    multiplier = modifiers.get('scale', 1.0)
    scaled_score = base_score * multiplier

    # Additional logic with red herring variables
    threshold = modifiers.get('threshold', 50)
    adjustment_factor = modifiers.get('factor', 0)  # Not actually used

    # Conditional penalty (never triggered due to fixed data)
    if scaled_score > 100:
        penalty_adjustment = 10  # Dead code path

    # String slicing distraction
    report_id = "PRF2024XYZ"
    year_segment = report_id[3:7]  # '2024' — unused

    # Dictionary manipulation that affects result
    corrections = {k: v for k, v in modifiers.items() if k in ['bonus', 'penalty']}
    final_score = scaled_score + corrections.get('bonus', 5) - corrections.get('penalty', 3)

    # Unused loop with side computation
    cumulative = 0
    for i in range(3):
        cumulative += i * 2  # Distractor: not used in result

    return final_score

# Input data
metrics = {
    'metric_response': 20,
    'metric_latency': 15,
    'metric_throughput': 30,
    'metric_error_rate': 10,
    'auxiliary_flag': 999  # Not included due to naming
}

adjustments = {
    'scale': 1.2,
    'bonus': 7,
    'penalty': 4,
    'threshold': 80,
    'factor': 0.5  # Misleading parameter
}

# Execution
final_score = process_performance(metrics, adjustments)
print(f"Result: {final_score}")