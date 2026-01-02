import math

def analyze_signal(samples):
    # Irrelevant preprocessing (distractor)
    normalized = [s / max(abs(min(samples)), abs(max(samples))) for s in samples]
    filtered = [x for x in normalized if abs(x) > 0.1]
    
    # Core computation path (hidden among distractions)
    magnitude = sum(abs(s) for s in samples)
    peak_to_avg_ratio = max(abs(s) for s in samples) / (sum(abs(s) for s in samples) / len(samples))
    
    # Red herring: unused transformation
    def envelope(signal):
        return [abs(signal[i]) + abs(signal[i-1]) for i in range(1, len(signal))]
    
    return magnitude, peak_to_avg_ratio

def transform_data(raw):
    # Destructuring and tuple unpacking (valid concept)
    a, b = zip(*[(x, x*2 + 1) for x in raw if x % 3 == 0])
    
    # Dead code path (irrelevant)
    if len(a) > 100:
        return list(map(lambda z: z * 0.5, a))
    else:
        temp_result = [val ** 0.5 for val in b if val > 0]
        # Unused variable (distractor)
        cumulative = 0
        for t in temp_result:
            cumulative += t
    
    # Actual relevant output
    return [b[i] - b[i-1] for i in range(1, len(b))] if len(b) > 1 else [0]

def evaluate_stability(readings):
    if not readings:
        return 0.0
    mean_val = sum(readings) / len(readings)
    variance = sum((r - mean_val) ** 2 for r in readings) / len(readings)
    return math.sqrt(variance)

def main_pipeline(input_data):
    # Multiple assignments and distractors
    backup_copy = input_data.copy()
    temp_storage = []
    
    for item in backup_copy:
        if item < 0:
            temp_storage.append(item ** 2)
        else:
            temp_storage.append(item)
    
    # Key data flow
    processed = [x for x in input_data if x % 2 == 1]  # Filter odd values
    
    # Decoy function definition (never called)
    def deprecated_handler(data):
        return [d << 2 for d in data]
    
    # Real processing steps
    magnitude, ratio = analyze_signal(processed)
    transformed_data = transform_data([int(magnitude % 100)] + [int(ratio * 10)] * 5)
    
    # Misleading intermediate (looks important but isn't)
    diagnostic_score = evaluate_stability([magnitude, ratio, len(processed)])
    
    # Threshold logic using lambda (required feature)
    threshold_func = lambda x: x > 5 and x != 13
    
    # Critical execution point
    final_diagnostic = process_metrics(transformed_data, threshold_func)
    
    # Unused result (distractor)
    summary_report = {'count': len(transformed_data), 'max': max(transformed_data), 'flagged': diagnostic_score > 1.5}
    
    return final_diagnostic

def process_metrics(values, condition):
    # Another layer of filtering
    valid_entries = [v for v in values if condition(v)]
    if not valid_entries:
        return -999
    
    # Final calculation
    avg = sum(valid_entries) / len(valid_entries)
    correction_factor = 1.75 if len(valid_entries) >= 3 else 0.85
    return round(avg * correction_factor, 4)

# Simulate input
sensor_input = [12, -7, 15, 22, 9, 3, 8, 11, 4, 6]

# Execute main logic
result_value = main_pipeline(sensor_input)

# Print final answer as required
print(f"Result: {result_value}")