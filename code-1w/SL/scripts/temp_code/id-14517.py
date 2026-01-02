def analyze_metrics(values):
    total = sum(values)
    avg = total / len(values) if values else 0
    variance = sum((x - avg) ** 2 for x in values) / len(values) if values else 0
    return avg, variance


def filter_outliers(data, threshold=2):
    mean, var = analyze_metrics(data)
    std_dev = var ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]


def calculate_final_score(raw_data):
    # Preprocessing step with potential distractions
    temp_stats = {}
    temp_stats['max_val'] = max(raw_data) if raw_data else 0
    temp_stats['min_val'] = min(raw_data) if raw_data else 0
    
    cleaned_data = filter_outliers(raw_data)
    
    # Simulate normalization (not directly used in final score)
    normalized = [(x - temp_stats['min_val']) / (temp_stats['max_val'] - temp_stats['min_val'] + 1e-8) for x in raw_data]
    
    # Core logic: count how many are above median
    sorted_data = sorted(cleaned_data)
    mid = len(sorted_data) // 2
    median_clean = (sorted_data[mid] + sorted_data[~mid]) / 2
    
    above_median = sum(1 for x in cleaned_data if x > median_clean)
    below_or_equal = len(cleaned_data) - above_median
    
    # Secondary metric (distraction)
    growth_rate = (cleaned_data[-1] - cleaned_data[0]) / cleaned_data[0] if cleaned_data and cleaned_data[0] != 0 else 0
    
    # Final scoring logic
    balance_factor = above_median - below_or_equal
    penalty = 0
    for i, val in enumerate(cleaned_data):
        if i % 3 == 0 and val < median_clean:
            penalty += 1
    
    base_score = len(cleaned_data) * 3
    final_score = base_score + balance_factor - (penalty * 2)
    
    # Irrelevant tracking variables (distractors)
    debug_info = []
    for idx, (i, v) in enumerate(enumerate(normalized)):
        debug_info.append(f"Step {idx}: index={i}, norm={v:.4f}")
    
    return final_score

# Main execution
sensor_readings = [12, 15, 10, 8, 30, 14, 13, 11, 9, 32, 16, 11, 7]

# Extraneous computation
shadow_copy = [x * 1.05 for x in sensor_readings]
sorted_shadow = sorted(shadow_copy, reverse=True)
avg_shadow = sum(sorted_shadow) / len(sorted_shadow)

processed_data = [x for x in sensor_readings if x >= 10]

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")