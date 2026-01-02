def analyze_performance(log, thresh):
    # Irrelevant transformation (distractor)
    normalized = [round(x * 0.95 + 2.3, 2) for x in log if x > 0]
    
    # Semi-relevant pre-processing
    filtered = [x for x in log if 10 <= x <= 100]
    
    # Red herring computation on transformed data
    avg_normalized = sum(normalized) / len(normalized) if normalized else 0
    deviation = [abs(x - avg_normalized) for x in normalized]
    
    # Actual logic begins: count how many metrics exceed threshold
    count_above = 0
    cumulative = 0
    for i, val in enumerate(filtered):
        if val > thresh:
            count_above += 1
            cumulative += val * (i + 1)  # Weight by position

    # Secondary metric that isn't used (dead path)
    redundancy_check = any(filtered.count(x) > 2 for x in set(filtered))
    
    # Key computation: efficiency score based on weighted sum and count
    if count_above == 0:
        return 0
    base_efficiency = cumulative / count_above
    
    # Bonus factor for early high performers (first third of filtered list)
    early_window = len(filtered) // 3 or 1
    early_bonus = sum(1 for i, v in enumerate(filtered[:early_window]) if v > thresh)
    
    final_score = base_efficiency + (early_bonus * 5.5)
    
    # Unused diagnostic print (distraction)
    debug_info = f'Detected {count_above} high-performers with {early_bonus} in early window'
    
    return int(final_score)

# Simulated system metrics (real input)
raw_readings = [85, 92, 45, 103, 78, 96, 110, 67, 94, 88, 91, 55]

# Irrelevant preprocessing chain
processed_data = list(map(lambda x: x + 1 if x < 100 else x - 5, raw_readings))
sorted_data = sorted(processed_data, reverse=True)
duplicate_filter = [x for i, x in enumerate(sorted_data) if x not in sorted_data[:i]]

# Threshold for performance analysis
operational_threshold = 87

# Core execution point
metrics_log = [x for x in raw_readings if x >= 50]  # Final relevant input
threshold = operational_threshold

# Critical statement
efficiency_score = analyze_performance(metrics_log, threshold)

# Output result
print(f"Result: {efficiency_score}")