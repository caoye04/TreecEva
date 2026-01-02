def analyze_conditions(data, config):
    warnings = 0
    critical_count = 0
    temp_sum = 0.0
    adjusted_values = []

    for i, val in enumerate(data):
        if val > config['max_limit']:
            warnings += 1
            adjusted_values.append(val * 0.9)
        elif val < config['min_limit']:
            critical_count += 1
            adjusted_values.append(val * 1.1)
        else:
            adjusted_values.append(val)

    avg_temp = sum(adjusted_values) / len(adjusted_values)
    return avg_temp, warnings, critical_count


def validate_readings(readings):
    valid = []
    outlier_score = 0
    for r in readings:
        if 15 <= r <= 35:
            valid.append(r)
        else:
            outlier_score += abs(r - 25)
    return valid, outlier_score


def calculate_rating(temp_log, limits):
    # Preprocessing step (distractor: not used in final logic)
    filtered_temps, _ = validate_readings(temp_log)
    
    base_config = {
        'max_limit': limits[0],
        'min_limit': limits[1]
    }
    
    mean_val, warn_count, crit_count = analyze_conditions(temp_log, base_config)
    
    # Distractor variables
    dummy_sum = 0
    for x in range(len(temp_log)):
        dummy_sum += x * 2  # Irrelevant computation
    
    # Key logic with intermediate distraction
    adjustment_factor = 1.0
    if warn_count > 0:
        adjustment_factor *= 0.95
    if crit_count > 0:
        adjustment_factor *= 0.90
    
    # Simulated historical baseline (dead code path)
    historical_avg = 22.5
    drift = abs(mean_val - historical_avg)
    if drift > 5:
        pass  # Placeholder for future action, no effect

    # Final scoring logic
    raw_score = mean_val * 10
    penalty = (warn_count * 2) + (crit_count * 5)
    final_score = (raw_score - penalty) * adjustment_factor
    
    # Additional irrelevant transformation
    normalized = [round(t / max(temp_log), 3) for t in temp_log]
    total_norm = sum(normalized)
    
    return int(final_score)

# Main execution context
if __name__ == "__main__":
    temperatures = [23, 18, 37, 25, 14, 29, 41, 20]
    thresholds = [35, 16]
    
    # Debugging traces (irrelevant to outcome)
    debug_stats = {"length": len(temperatures), "peak": max(temperatures)}
    cumulative = 0
    for idx, t in enumerate(temperatures):
        cumulative += t
        if cumulative > 100:
            break
    
    final_score = calculate_rating(temperatures, thresholds)
    print(f"Result: {final_score}")