import math

# Simulated sensor fusion system for environmental monitoring
def collect_sensor_data():
    raw_readings = [23.4, 18.9, 25.1, 22.0, 19.8, 24.3, 20.2, 21.7]
    timestamps = [1623456780, 1623456785, 1623456790, 1623456795, 1623456800, 1623456805, 1623456810, 1623456815]
    sensor_ids = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8']
    
    # Irrelevant aggregation (distractor)
    avg_temp = sum(raw_readings) / len(raw_readings)
    max_temp = max(raw_readings)
    min_temp = min(raw_readings)
    temp_range = max_temp - min_temp
    
    # Red herring computation
    stability_score = (1 / (temp_range + 1)) * 100
    
    # Actual data bundle (only this is used later)
    return list(zip(sensor_ids, timestamps, raw_readings))

# Filtering module with decoy logic
def filter_anomalies(data):
    # Extract readings for analysis
    readings_only = [entry[2] for entry in data]
    median_val = sorted(readings_only)[len(readings_only)//2]
    deviation_threshold = 2.5
    
    # Distractor: unused statistical measures
    mean_val = sum(readings_only) / len(readings_only)
    variance = sum((x - mean_val)**2 for x in readings_only) / len(readings_only)
    std_dev = math.sqrt(variance)
    z_scores = [(x - mean_val) / std_dev for x in readings_only]
    
    # Another red herring: hypothetical prediction model (unused)
    predicted_next = mean_val * 1.02 - (std_dev * 0.5)
    confidence_interval = (mean_val - 1.96*std_dev, mean_val + 1.96*std_dev)
    
    # Real filtering logic based on median deviation
    filtered = [entry for entry in data if abs(entry[2] - median_val) <= deviation_threshold]
    return filtered

# Signal processing with multiple abstraction layers
def analyze_phase_shift(readings):
    # Simulate frequency domain transformation
    phase_values = []
    for i, val in enumerate(readings):
        phase = math.sin(val * math.pi / 180) * math.cos(i * math.pi / 4)
        phase_values.append(phase)
    
    # Decoy energy calculation
    signal_energy = sum(p**2 for p in phase_values)
    
    # Real metric: average coherent phase
    coherent_phase = sum(abs(p) for p in phase_values) / len(phase_values)
    return coherent_phase

# Main processing pipeline
def process_readings(filtered_data):
    # Extract cleaned temperatures
    temps = [entry[2] for entry in filtered_data]
    
    # Destructuring assignment distraction
    first, *middle, last = temps
    mid_length = len(middle)
    
    # Set operation to eliminate duplicates (though none expected)
    unique_temps = set(temps)
    duplicate_count = len(temps) - len(unique_temps)
    
    # Dictionary-based categorization (partly irrelevant)
    temp_categories = {}
    for t in temps:
        category = 'cool' if t < 20 else 'warm' if t < 23 else 'hot'
        temp_categories[t] = category
    
    # Count distribution (distractor)
    category_counts = {k: 0 for k in ['cool', 'warm', 'hot']}
    for cat in temp_categories.values():
        category_counts[cat] += 1
    
    # Slicing operations on temperature sequence
    window_1 = temps[:3]
    window_2 = temps[1:4]
    window_3 = temps[-3:]
    
    # Compute overlapping similarity (red herring)
    common_in_windows = len(set(window_1) & set(window_2) & set(window_3))
    
    # Real computational chain
    base_metric = sum(temps) / len(temps)
    fluctuation = max(temps) - min(temps)
    
    # Nested conditional with misleading branches
    adjustment_factor = 0
    if fluctuation < 1.0:
        adjustment_factor = 0.1
    elif fluctuation < 2.0:
        adjustment_factor = 0.25
    else:
        if base_metric < 21:
            adjustment_factor = 0.4  # This branch taken
        else:
            adjustment_factor = 0.35
    
    # Multi-step derivation with modular arithmetic
    sample_count = len(temps)
    checksum = sum(temps[i] * (i + 1) for i in range(len(temps)))
    normalized_checksum = checksum % 100
    
    # Critical intermediate values
    phase_analysis = analyze_phase_shift(temps)
    trend_weight = math.log(sample_count + 1) * phase_analysis
    
    # Final integration formula
    diagnostic_score = (base_metric * 1.5) + (trend_weight * 2.0) - (adjustment_factor * 10)
    final_diagnostic = int(diagnostic_score * 10)  # Scale and truncate
    
    # Dead code path (never executed - distractor)
    if False:
        backup_system = {'status': 'offline', 'last_sync': None}
        for k in backup_system:
            backup_system[k] = 'reset'
        return backup_system['status']
    
    return final_diagnostic

# Execution flow
sensor_data = collect_sensor_data()
filtered_sensors = filter_anomalies(sensor_data)
final_diagnostic = process_readings(filtered_sensors)
print(f"Target result: {final_diagnostic}")