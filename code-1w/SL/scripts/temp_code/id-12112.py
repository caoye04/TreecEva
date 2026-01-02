import math

# Simulated sensor data processing with diagnostic logic
def process_sensor_readings(raw_readings, calibration_factor):
    calibrated = [x * calibration_factor for x in raw_readings]
    smoothed = []
    for i in range(len(calibrated)):
        if i == 0:
            smoothed.append(calibrated[i])
        else:
            smoothed.append(0.7 * calibrated[i] + 0.3 * smoothed[i-1])
    return smoothed

# Irrelevant helper - dead path
def deprecated_filter(data):
    return [x for x in data if x > 0]

# Data transformation pipeline
def transform_signal(signal_data):
    squared = [x ** 2 for x in signal_data]
    shifted = [x / 2.0 for x in squared]
    # Decoy transformation
    inverted = [1 / (1 + x) for x in squared if x != 0]
    normalized = [x / max(shifted) for x in shifted]
    return normalized

# Complex condition evaluator
def evaluate_stability(metrics, tolerance=0.05):
    variance = sum((x - sum(metrics)/len(metrics))**2 for x in metrics) / len(metrics)
    return variance < tolerance

# Unused recursive red herring
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Real pattern analyzer with critical logic
def analyze_pattern(seq, threshold_fn):
    count_above = 0
    cumulative = 0
    for val in seq:
        if threshold_fn(val):
            count_above += 1
            cumulative += val
    return int(cumulative * 1000) if count_above > 0 else -1

# Misleading intermediate diagnostics
interim_results = []
def log_diagnostics(name, value):
    interim_results.append({"name": name, "value": value})  # Dead logging

# High-interference main flow
if __name__ == "__main__":
    raw_input_stream = [0.1, 0.15, 0.08, 0.22, 0.18, 0.11, 0.09, 0.14]
    config_scale = 1.08
    
    # Step 1: Process sensor input
    filtered_data = process_sensor_readings(raw_input_stream, config_scale)
    
    # Step 2: Transform signal (critical path)
    transformed_data = transform_signal(filtered_data)
    
    # Step 3: Setup evaluation context
    stability_check = evaluate_stability(transformed_data, tolerance=0.03)
    log_diagnostics("preliminary", sum(transformed_data))
    
    # Step 4: Define dynamic threshold using lambda (required feature)
    dynamic_t = 0.5 * max(transformed_data)
    threshold_func = lambda x: x > dynamic_t
    
    # Step 5: Evaluate combinatorics-based side metric (distractor)
    combination_count = 0
    for i in range(len(transformed_data)):
        for j in range(i+1, len(transformed_data)):
            if abs(transformed_data[i] - transformed_data[j]) < 0.1:
                combination_count += 1
    log_diagnostics("combinatoric_match", combination_count)
    
    # Step 6: Final diagnostic analysis (key statement)
    final_diagnostic = analyze_pattern(transformed_data, threshold_func)
    
    # Print result as required
    print(f"Result: {final_diagnostic}")