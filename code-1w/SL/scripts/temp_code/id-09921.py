import math

# Simulated sensor network data processing with diagnostic logic
def collect_sensor_readings():
    raw_readings = [
        (101, 23.4, 1), (102, 25.1, 0), (103, 19.8, 1),
        (104, 30.5, 0), (105, 27.3, 1), (106, 22.0, 1),
        (107, 28.9, 0), (108, 26.7, 1)
    ]
    return raw_readings

# Irrelevant helper - distractor
def calculate_checksum(data):
    checksum = 0
    for item in data:
        if isinstance(item, tuple):
            checksum ^= hash(item)
    return checksum % 1000

# Noise filter using median smoothing - relevant
def smooth_signal(signal):
    sorted_vals = sorted(signal)
    mid = len(sorted_vals) // 2
    median = sorted_vals[mid] if len(sorted_vals) % 2 else (sorted_vals[mid-1] + sorted_vals[mid]) / 2
    return [x if abs(x - median) < 10 else median for x in signal]

# Unused function - dead code path (distractor)
def legacy_compatibility_mode():
    config_flags = {"mode": "legacy", "version": 1.0}
    buffer = [0] * 256
    return sum(buffer) + hash(str(config_flags))

# Main preprocessing pipeline
def preprocess_readings(raw_readings):
    ids, temps, statuses = zip(*raw_readings)
    temp_floats = [float(t) for t in temps]
    
    # Apply noise reduction
    cleaned_temps = smooth_signal(temp_floats)
    
    # Distractor variables
    avg_temp = sum(cleaned_temps) / len(cleaned_temps)
    temp_variance = sum((t - avg_temp) ** 2 for t in cleaned_temps) / len(cleaned_temps)
    entropy_proxy = -sum(t * math.log(t) for t in cleaned_temps if t > 0) if cleaned_temps else 0
    
    # Normalize status codes
    active_count = sum(statuses)
    normalized_health = [1 if s == 1 else -1 for s in statuses]
    
    # Create enriched tuples with dummy padding (irrelevant fields)
    enriched = []
    for i, (id_val, temp, orig_status) in enumerate(raw_readings):
        dummy_flag = (id_val * 7 + 13) % 19
        padded_entry = (id_val, temp, orig_status, dummy_flag, math.sin(temp))
        enriched.append(padded_entry)
    
    # Use enumerate to align indices (relevant for later mapping)
    indexed_data = [(idx, entry) for idx, entry in enumerate(enriched)]
    return indexed_data, cleaned_temps, normalized_health

# Threshold policy configuration - relevant
def generate_threshold_map(base_offset=2.5):
    levels = ['low', 'medium', 'high']
    base_values = {'low': 20.0 - base_offset, 'medium': 25.0, 'high': 30.0 + base_offset}
    safety_offsets = {key: val * 0.05 for key, val in base_values.items()}
    
    # Distractor computation
    total_influence = sum(base_values.values()) * sum(safety_offsets.values())
    adjustment_factor = math.sqrt(total_influence) / 100
    
    final_map = {level: base_values[level] + safety_offsets[level] + adjustment_factor 
                 for level in levels}
    return final_map, adjustment_factor

# Core analysis engine
def analyze_readings(processed_data, threshold_map):
    _, data_entries = processed_data
    readings_list = [entry[1][1] for entry in data_entries]  # Extract temperature
    id_list = [entry[1][0] for entry in data_entries]
    
    # Misleading intermediate aggregation
    peak_reading = max(readings_list)
    reading_range = max(readings_list) - min(readings_list)
    fluctuation_score = reading_range * len(readings_list)
    
    # Actual decision logic
    medium_thresh = threshold_map['medium']
    high_thresh = threshold_map['high']
    
    above_medium = sum(1 for r in readings_list if r >= medium_thresh)
    above_high = sum(1 for r in readings_list if r >= high_thresh)
    
    # Weighted diagnostic score
    severity_weight = 3.0 if above_high > 1 else 1.5
    stability_penalty = 0.8 if fluctuation_score > 20 else 1.0
    
    # Distractor: unused complex structure
    diagnostic_profile = {
        'metrics': {
            'peak': peak_reading,
            'variance': fluctuation_score / len(readings_list),
            'entropy': math.log(fluctuation_score + 1)
        },
        'flags': [f"ID{id_list[i]}" for i in range(len(id_list)) if readings_list[i] > medium_thresh],
        'checksum': calculate_checksum(readings_list)
    }
    
    # Critical calculation - this determines the answer
    base_score = sum(math.ceil(r) for r in readings_list)
    adjustment = above_medium * severity_weight * stability_penalty
    final_diagnostic = int(base_score - adjustment)
    
    return final_diagnostic

# Orchestration
if __name__ == "__main__":
    # Collect raw input
    raw_data = collect_sensor_readings()
    
    # Preprocess with multiple side computations
    processed_result = preprocess_readings(raw_data)
    processed_data, cleaned_temps, health_status = processed_result
    
    # Generate dynamic thresholds
    threshold_map, adj_factor = generate_threshold_map(base_offset=2.5)
    
    # Execute main analysis
    final_diagnostic = analyze_readings(processed_data, threshold_map)
    
    # Output target result
    print(f"Result: {final_diagnostic}")