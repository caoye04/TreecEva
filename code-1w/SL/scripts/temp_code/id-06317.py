def calculate_final_score(data, thresholds):
    # Precompute some statistics (some are distractions)
    total_entries = len(data)
    valid_count = 0
    temp_sum = 0.0
    outlier_flags = []
    
    # Irrelevant intermediate computation (distractor)
    squared_magnitudes = [x**2 for x in data if x > 0]
    avg_square = sum(squared_magnitudes) / len(squared_magnitudes) if squared_magnitudes else 0

    # Track state across iterations
    running_tally = 0
    penalty_adjustment = 0
    
    for i, value in enumerate(data):
        # Outlier detection based on thresholds (semi-relevant)
        is_outlier = any(value < t for t in thresholds)
        outlier_flags.append(is_outlier)
        
        # Core logic: only values within all thresholds contribute
        if not is_outlier:
            temp_sum += value
            valid_count += 1
        
        # Additional distraction: simulate lagged adjustment
        if i % 3 == 0 and value > 50:
            penalty_adjustment -= 2  # minor red herring

    # Secondary processing with zip (required feature)
    paired_data = list(zip(data[:-1], data[1:]))
    trend_corrections = [b - a for a, b in paired_data if a < b]  # misleading metric
    trend_penalty = len(trend_corrections) // 4  # has minimal impact

    # Final scoring logic
    base_score = temp_sum / valid_count if valid_count > 0 else 0
    adjustment_factor = 1 + (penalty_adjustment * 0.01)
    final_score = base_score * adjustment_factor - trend_penalty

    return int(final_score)

# Main execution
raw_values = [85, 72, 90, 45, 68, 77, 53, 95, 60, 70]
thresholds = [40, 48, 55]  # must be above all to count as valid
final_score = calculate_final_score(raw_values, thresholds)
print(f"Result: {final_score}")