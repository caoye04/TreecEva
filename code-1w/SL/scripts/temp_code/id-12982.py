import math

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    return sum([x * math.log(x) for x in data if x > 0])

# Misleading transformation with dead-end logic
def transform_metrics(values):
    temp = [v ** 0.5 for v in values]
    offset = sum(temp) / len(temp)
    adjusted = [t - offset + 2.5 for t in temp]  # Never used
    return [round(x, 2) for x in temp]

# Core processing function with red herring parameters
def filter_outliers(dataset, threshold=3.0, mode='strict'):
    mean_val = sum(dataset) / len(dataset)
    std_dev = (sum((x - mean_val) ** 2 for x in dataset) / len(dataset)) ** 0.5
    filtered = [x for x in dataset if abs(x - mean_val) / std_dev < threshold]
    
    # Distractor: unused conditional branch
    if mode == 'relaxed':
        fallback = [x for x in dataset if x > mean_val - 2 * std_dev]
        return fallback
    
    return filtered

# Simulate sensor node aggregation (partially relevant)
def aggregate_nodes(raw_readings):
    logs = []
    results = []
    for i, reading in enumerate(raw_readings):
        if i % 3 == 0:
            logs.append(f"Node {i} synced")
        processed = (reading * 1.8) + 32  # Convert to Fahrenheit (irrelevant)
        results.append(reading * 0.75)  # Only this matters
    return results

# Intermediate transformation with list comprehension and filtering
def normalize_sequence(seq):
    min_val, max_val = min(seq), max(seq)
    range_val = max_val - min_val if max_val != min_val else 1
    normalized = [(x - min_val) / range_val for x in seq]
    scaled = [int(x * 1000) for x in normalized]
    trimmed = [x for x in scaled if x > 100]  # Filter out small values
    return trimmed

# Critical path: process nodes through multiple stages
def finalize_calibration(calibrated_list):
    base = sum(calibrated_list)
    factor = len(calibrated_list) ** 0.5
    adjustment = math.sin(math.pi / 6)  # Constant = 0.5
    result = base * factor * adjustment
    
    # Red herring: complex but unused expression
    secondary_correction = sum([
        (i + 1) * val / 100 for i, val in enumerate(calibrated_list)
        if val % 2 == 0
    ]) - len(calibrated_list)
    
    return int(result)

# --- MAIN EXECUTION WITH DISTRACTORS ---
if __name__ == "__main__":
    # Initial sensor data (real input)
    sensor_input = [120, 150, 90, 200, 180, 220, 100, 130]

    # Irrelevant entropy calculation (dead code path)
    entropy_values = [0.1, 0.4, 0.35, 0.8, 0.6]
    system_entropy = calculate_entropy(entropy_values)

    # Apply misleading transformation
    transformed = transform_metrics(sensor_input)

    # Filter outliers — actual impact on data
    cleaned_data = filter_outliers(sensor_input, threshold=2.5)

    # Aggregate nodes — only uses raw readings
    aggregated = aggregate_nodes(cleaned_data)

    # Normalize sequence — modifies scale
    normalized_output = normalize_sequence(aggregated)

    # Decoy operation: tuple unpacking with dummy variables
    summary_stats = (sum(normalized_output), len(normalized_output), max(normalized_output))
    total, count, peak = summary_stats

    # Simulated calibration curve using list comprehension
    calibration_curve = [
        int(50 + (i * 7.3)) for i in range(count)
        if i % 2 == 1 or i == 0
    ]

    # Processed nodes: intersect normalized output with calibration thresholds
    processed_nodes = [
        n for n in normalized_output 
        if any(abs(n - c) < 80 for c in calibration_curve)
    ]

    # Final computation — KEY STATEMENT
    thermal_capacity = finalize_calibration(processed_nodes)

    # Additional distractor: unused recursive function
    def predict_decay(levels, depth=0):
        if depth >= 3 or not levels:
            return [l // 2 for l in levels]
        return predict_decay([l - 5 for l in levels], depth + 1)

    # Output target result
    print(f"Result: {thermal_capacity}")