from itertools import combinations

# Simulate sensor readings with noise filtering and performance evaluation
def analyze_sensor_data(readings):
    filtered = [r for r in readings if 10 <= r <= 100]
    
    # Irrelevant transformation: frequency analysis (not used in final score)
    freq_map = {}
    for r in filtered:
        freq_map[r] = freq_map.get(r, 0) + 1
    
    # Misleading intermediate: average after outlier removal (partially relevant)
    sorted_vals = sorted(filtered)
    trim_count = len(sorted_vals) // 10
    trimmed = sorted_vals[trim_count:-trim_count] if trim_count > 0 else sorted_vals
    mean_trimmed = sum(trimmed) / len(trimmed) if trimmed else 0
    
    # Distractor: harmonic mean calculation (unused)
    harmonic_mean = 0
    if any(v > 0 for v in trimmed):
        harmonic_mean = len(trimmed) / sum(1/v for v in trimmed if v > 0)
    
    # Key metric: variance of top quartile values
    top_quartile = sorted_vals[int(0.75 * len(sorted_vals)):] if len(sorted_vals) > 0 else [0]
    mean_top = sum(top_quartile) / len(top_quartile)
    variance = sum((x - mean_top) ** 2 for x in top_quartile) / len(top_quartile)
    
    # Secondary metric: count of stable sequences
    stability_runs = 0
    current_run = 0
    for i in range(1, len(filtered)):
        if abs(filtered[i] - filtered[i-1]) < 5:
            current_run += 1
        else:
            if current_run > 2:
                stability_runs += 1
            current_run = 0
    if current_run > 2:
        stability_runs += 1

    # Complex conditional expression combining metrics
    base_score = 75 if variance < 50 else (85 if variance < 200 else 60)
    adjustment = 10 if stability_runs >= 2 else (5 if stability_runs == 1 else -8)
    
    # Final logic using slicing and conditional override
    recent_trend = filtered[-3:] if len(filtered) >= 3 else filtered
    trend_slope = (recent_trend[-1] - recent_trend[0]) / (len(recent_trend) - 1) if len(recent_trend) > 1 else 0
    
    # Critical decision point
    performance_bonus = 15 if trend_slope > 3 and base_score > 80 else (10 if trend_slope > 1 else 0)
    
    # Final score computation
    final_score = base_score + adjustment + performance_bonus
    
    # Dead code path - never executed due to prior filtering
    if any(r < 0 for r in readings):
        final_score -= 20  # unreachable
    
    return final_score

# Generate deterministic synthetic data
raw_readings = [12, 15, 14, 98, 99, 100, 97, 25, 27, 26, 28, 30, 33, 35, 34, 36, 38, 40, 42, 45]

# Extra unused helper (distractor)
def moving_average(data, window=3):
    return [sum(data[i:i+window]) / window for i in range(len(data)-window+1)]

# Unused combination analysis
pairwise_diffs = list(combinations(raw_readings[::5], 2))

# Main execution
final_score = analyze_sensor_data(raw_readings)
print(f"Result: {final_score}")