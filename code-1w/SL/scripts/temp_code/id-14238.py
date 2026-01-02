import math

# Simulated sensor data processing for environmental monitoring system
def collect_sensor_data():
    raw_values = [23.4, 19.1, 25.6, 20.3, 18.9, 22.7, 24.8, 21.0, 19.5, 26.2]
    baseline = 20.5
    adjusted = [round(x - baseline, 2) for x in raw_values]
    return adjusted

# Irrelevant helper: calculates entropy (not used in final result)
def calculate_entropy(data):
    total = sum(data)
    if total == 0:
        return 0.0
    probs = [abs(x / total) for x in data if x != 0]
    entropy = -sum(p * math.log2(p) for p in probs)
    return round(entropy, 4)

# Decoy function: looks important but unused
def validate_checksum(arr):
    checksum = 0
    for i, val in enumerate(arr):
        checksum ^= int(val * 100) + i
    return checksum % 256

# Real processing chain starts here
def filter_outliers(data, threshold=3.0):
    mean_val = sum(data) / len(data)
    variance = sum((x - mean_val) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    filtered = [x for x in data if abs(x) <= threshold * std_dev]
    return filtered, mean_val, std_dev

# Complex transformation with distractors
def transform_readings(readings):
    # Distractor variables
    temp_buffer = []
    history_log = set()
    cumulative = 0
    
    for val in readings:
        cumulative += abs(val)
        temp_buffer.append(abs(val) ** 1.5)
        history_log.add(round(val, 1))
    
    # Real computation path
    transformed = [math.sin(x) * 100 for x in readings]
    normalized = [round(t, 2) for t in transformed]
    
    # Dead code path - never accessed
    if len(history_log) > 100:
        fallback = sum(temp_buffer) / cumulative
        return [fallback] * len(readings)
    
    return normalized

# Aggregation with set operations (required language feature)
def aggregate_metrics(samples):
    positive_set = {i for i, x in enumerate(samples) if x > 0}
    negative_set = {i for i, x in enumerate(samples) if x < 0}
    neutral_indices = {i for i, x in enumerate(samples) if -0.5 <= x <= 0.5}
    
    # Meaningful intersection: detect stable fluctuations
    stable_variance = len(neutral_indices & positive_set)  # Always 0, red herring
    
    # Actual metric
    magnitude_score = sum(abs(x) for x in samples) / len(samples)
    peak_count = len(positive_set | negative_set)
    
    # Distractor: complex but unused structure
    stats_summary = {
        'range': max(samples) - min(samples),
        'density': peak_count / (magnitude_score + 1e-8),
        'consistency': len(positive_set) / len(samples)
    }
    
    return magnitude_score, peak_count

# Main processing pipeline
def process_logs(raw_adjusted):
    # First stage: filter
    filtered_data, base_mean, dev = filter_outliers(raw_adjusted)
    
    # Second stage: transform
    processed = transform_readings(filtered_data)
    
    # Third stage: aggregate
    score, count = aggregate_metrics(processed)
    
    # Introduce decoy variable that looks like final answer
    diagnostic_code = (count * 1000) + int(base_mean * 10)
    
    # Hidden intermediate (misleading)
    temp_result = math.floor(score * dev * 10) if dev > 0 else 0
    
    return {
        'readings': processed,
        'diagnostic': diagnostic_code,  # Red herring
        'temporal_marker': temp_result, # Distraction
        'final_score': score         # Relevant but not final
    }

# Final analysis with correct dependency chain
def analyze_readings(log_dict):
    readings = log_dict['readings']
    initial_score = log_dict['final_score']
    
    # Use set operations meaningfully
    high_activity = {i for i, r in enumerate(readings) if r > 50}
    low_activity = {i for i, r in enumerate(readings) if r < -50}
    volatility_set = high_activity | low_activity
    
    # Core calculation
    base_value = sum(readings) / len(readings)
    adjustment_factor = len(volatility_set) * 0.75
    
    # Critical statement
    final_diagnostic = int(base_value + adjustment_factor + initial_score)
    
    # Unused but plausible alternate path
    if len(high_activity) == 0 and len(low_activity) == 0:
        fallback = len(readings) * 2
        return fallback
    
    return final_diagnostic

# Execution flow
if __name__ == "__main__":
    # Step 1: Collect data
    raw_deviation = collect_sensor_data()
    
    # Step 2: Process logs (contains multiple distractions)
    processed_logs = process_logs(raw_deviation)
    
    # Step 3: Analyze readings - KEY EXECUTION POINT
    final_diagnostic = analyze_readings(processed_logs)
    
    # Print target result
    print(f"Target result: {final_diagnostic}")