def calculate_efficiency(data, limit):
    filtered = [x for x in data if x > limit]
    total = sum(filtered)
    count = len(filtered)
    if count == 0:
        return 0
    average = total / count
    
    # Distractor: irrelevant computation on transformed data
    squared_devs = [(x - average) ** 2 for x in filtered]
    variance = sum(squared_devs) / count if count > 1 else 0
    stability_factor = (variance + 1) / (average + 1)
    
    # More distraction: unused path involving secondary metric
    peak_value = max(data)
    normalized_peak = peak_value / (max(filtered) + 1e-5)
    adjustment = 1.0
    if normalized_peak > 0.9:
        adjustment = 0.95
    elif normalized_peak > 0.7:
        adjustment = 0.98
    else:
        adjustment = 1.0
    
    # Core logic embedded amidst noise
    base_score = average * count
    penalty = 0
    for val in data:
        if val < limit * 0.5:
            penalty += 1
    efficiency = base_score - (penalty * 2)
    
    # Final score calculation – only this matters
    return int(efficiency * adjustment)

# Simulated sensor readings
raw_readings = [12, 15, 8, 23, 45, 7, 19, 14, 30, 22, 11, 50, 3, 6, 18]

# Irrelevant preprocessing
shifted_values = [x - 5 for x in raw_readings if x > 10]
duplicate_check = [x for x in raw_readings if raw_readings.count(x) > 1]

# Data transformation with partial relevance
processed_data = [x * 1.1 for x in raw_readings]
processed_data = [int(x) for x in processed_data]  # Discretize

# Threshold for filtering relevant entries
target_baseline = 15
threshold = target_baseline * 0.8  # 12

# Secondary distractor variables
outlier_count = sum(1 for x in processed_data if x < 5 or x > 40)
scaling_factor = outlier_count / len(processed_data) if outlier_count else 0.0

# Key computation
efficiency_score = calculate_efficiency(processed_data, threshold)

# Output result as required
print(f"Result: {efficiency_score}")