def analyze_metrics(raw_values):
    normalized = [round(v / max(raw_values), 3) for v in raw_values]
    outliers = {i for i, v in enumerate(normalized) if v > 0.9}
    return normalized, outliers


def validate_inputs(entries):
    valid = []
    for entry in entries:
        if isinstance(entry, str) and len(entry) > 0:
            cleaned = entry.strip().lower()
            parts = cleaned.split(',')
            numeric_parts = [float(p) for p in parts if p.replace('.', '').isdigit()]
            if len(numeric_parts) >= 2:
                valid.append(numeric_parts)
    return valid


def calculate_performance(dataset):
    # Irrelevant preprocessing (distractor)
    temp_buffer = []
    for item in dataset:
        temp_buffer.extend(item)
    
    # Key transformation
    flattened = [val for row in dataset for val in row]
    avg = sum(flattened) / len(flattened)
    
    # Misleading variance calculation (not used)
    var_buffer = [(x - avg) ** 2 for x in flattened]
    computed_variance = sum(var_buffer) / len(var_buffer) if var_buffer else 0
    
    # State tracking with semi-relevant logic
    state_log = {}
    threshold = avg * 0.75
    above_threshold_count = 0
    for idx, val in enumerate(flattened):
        if val > threshold:
            above_threshold_count += 1
            state_log[idx] = 'high'
        else:
            state_log[idx] = 'low'
    
    # Secondary filtering (partially relevant)
    filtered_vals = list(filter(lambda x: x >= threshold, flattened))
    filtered_sum = sum(filtered_vals)
    
    # Dummy control flow (dead path)
    correction_factor = 1.0
    if len(filtered_vals) > 100:
        correction_factor = 0.95  # Never triggered
    elif len(filtered_vals) < 1:
        correction_factor = 1.1  # Also not triggered
    
    # Core logic contributing to answer
    base_score = filtered_sum * above_threshold_count
    adjustment = len(state_log.get('high', []))  # Always 0, misleading
    final_component = base_score / (avg + 1) if avg != -1 else base_score
    
    # Final assignment
    final_score = int(final_component * correction_factor)
    
    # Unrelated counters (distractors)
    total_iterations = 0
    for _ in range(len(flattened)):
        for _ in range(2):
            total_iterations += 1
    
    # Unused dictionary aggregation
    stats_summary = {
        'count': len(flattened),
        'high_count': above_threshold_count,
        'threshold': threshold,
        'iterations': total_iterations
    }
    
    return final_score

# Simulated input data
input_strings = [
    '3.4, 2.1, 5.6',
    '4.2, 7.8, 6.3',
    '5.5, 4.8, 9.1',
    '6.7, 5.2, 8.3',
    '7.0, 6.9, 5.8'
]

cleaned_data = validate_inputs(input_strings)
normalized_data, detected_outliers = analyze_metrics([sum(row) for row in cleaned_data])
benchmark_data = [[v * 1.1 for v in row] for row in cleaned_data]

# Execute key statement
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")