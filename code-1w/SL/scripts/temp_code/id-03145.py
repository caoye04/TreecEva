def analyze_metrics(data):
    baseline = sum(data) / len(data)
    variance = sum((x - baseline) ** 2 for x in data) / len(data)
    adjusted_values = [x * 0.9 if x > baseline else x * 1.1 for x in data]
    return adjusted_values

benchmark_data = [85, 90, 78, 92, 88, 76, 95]

def evaluate_stability(values):
    peak = max(values)
    trough = min(values)
    range_ratio = (peak - trough) / peak
    normalized = [v / peak for v in values]
    return range_ratio > 0.2, normalized

def calculate_performance(raw):
    processed = analyze_metrics(raw)
    is_unstable, scaled = evaluate_stability(processed)
    
    # Distractor: irrelevant computation on copy
    temp_snapshot = processed.copy()
    outlier_count = 0
    for val in temp_snapshot:
        if val < 70:
            outlier_count += 1
    
    # Real logic starts here
    high_performers = [s for s in scaled if s >= 0.85]
    bonus_factor = 1.2 if len(high_performers) >= 2 else 1.0
    base_score = sum(scaled) * 10
    
    # Additional distraction: unused transformation
    transformed_score = base_score * 0.95
    adjustment_log = {"original": base_score, "adjusted": transformed_score}
    
    final_score = base_score * bonus_factor
    
    # More red herring variables
    average_scaled = sum(scaled) / len(scaled)
    penalty_applied = False
    if average_scaled < 0.8:
        final_score *= 0.9
        penalty_applied = True
    
    return final_score

# Key execution point
target_data = benchmark_data[:]
final_score = calculate_performance(benchmark_data)
print(f"Result: {final_score}")