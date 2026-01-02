def analyze_efficiency(data):
    if not data:
        return 0
    total = sum(data)
    count = len(data)
    average = total / count
    variance = sum((x - average) ** 2 for x in data) / count
    efficiency = (average / (variance + 1)) if variance > 0 else average
    return efficiency

# Simulate system health metrics
temperature_readings = [23.5, 24.1, 22.9, 25.0, 23.8]
cpu_loads = [0.65, 0.72, 0.58, 0.81, 0.69]
memory_usage = [0.45, 0.52, 0.48, 0.61, 0.55]

# Distractor: irrelevant sensor data
humidity_levels = [45.2, 47.1, 44.8, 46.5, 45.9]
light_intensity = [320, 340, 310, 360, 330]

# Process relevant metrics
temp_efficiency = analyze_efficiency(temperature_readings)
cpu_efficiency = analyze_efficiency([1 - x for x in cpu_loads])
mem_efficiency = analyze_efficiency([1 - x for x in memory_usage])

# Combine into evaluation framework
metrics = {
    'thermal': temp_efficiency,
    'compute': cpu_efficiency,
    'storage': mem_efficiency
}

# Weight mapping using dictionary operations
weights = {
    'thermal': 0.4,
    'compute': 0.35,
    'storage': 0.25
}

# Use lambda to filter significant metrics above threshold
threshold_filter = lambda val: val > 0.5
significant_metrics = set(key for key, val in metrics.items() if threshold_filter(val))

# Irrelevant set operation (distractor)
all_categories = {'thermal', 'compute', 'storage', 'network', 'security'}
potential_overlap = all_categories & significant_metrics

# Composite scoring with distractor variables
drift_compensation = 0.087
normalization_factor = 1.0 / sum(weights.values())  # Should be 1.0

# Core calculation logic
def evaluate_performance(met, wts):
    base_score = sum(met[k] * wts[k] for k in met)
    
    # Extra logic that doesn't affect final result
    outlier_flags = []
    for key, val in met.items():
        if val < 0.3 or val > 1.2:
            outlier_flags.append(key)
    
    # Unused correction attempt
    adjustment = 0
    if 'compute' in potential_overlap and 'thermal' not in potential_overlap:
        adjustment = -0.05
    
    # Final score unaffected by adjustment
    final_raw = base_score * normalization_factor
    
    # Additional red herring computation
    synthetic_index = (met['thermal'] ** 2 + met['compute'] * met['storage']) / 3
    
    return int(final_raw * 100) / 100.0

# Execute main evaluation
final_score = evaluate_performance(metrics, weights)

# Print result as required
print(f"Result: {final_score}")