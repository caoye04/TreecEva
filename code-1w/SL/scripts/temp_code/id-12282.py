def analyze_temperatures(raw_readings):
    # Normalize temperature data
    celsius_values = [round(temp - 273.15, 2) for temp in raw_readings]
    positive_only = [t for t in celsius_values if t > 0]
    high_temps = set([t for t in positive_only if t > 25])
    
    # Irrelevant statistical distraction
    mean_temp = sum(celsius_values) / len(celsius_values) if celsius_values else 0
    variance_proxy = sum((t - mean_temp) ** 2 for t in celsius_values) / len(celsius_values) if celsius_values else 0
    fluctuation_index = int(variance_proxy * 10) % 7  # Unused later

    # Core processing
    temp_buckets = {}
    for t in celsius_values:
        bucket = int(t // 5)
        temp_buckets[bucket] = temp_buckets.get(bucket, 0) + 1
    
    # Identify frequent moderate temps (10-25°C)
    moderate_range_vals = [t for t in celsius_values if 10 <= t <= 25]
    stability_score = len(moderate_range_vals) * 2

    # Bitwise weighting based on bucket diversity
    unique_buckets = set(temp_buckets.keys())
    diversity_flag = len(unique_buckets) & 7  # Lower 3 bits of bucket count
    adjusted_stability = stability_score ^ diversity_flag  # XOR adjustment

    return adjusted_stability, high_temps


def calculate_final_score(data_tuple):
    base_score, hot_temps = data_tuple
    
    # Auxiliary transformation
    scaled_score = base_score * 3
    penalty = 0
    
    # Conditional penalties
    if len(hot_temps) > 2:
        penalty += 15
    elif len(hot_temps) == 0:
        penalty += 5
    
    # Red herring calculation
    phantom_risk = 0
    for _ in range(3):
        phantom_risk += (base_score % 11) * 0.5  # Not used in final result
    
    # Final computation
    final_score = scaled_score - penalty
    
    # Debugging artifact (no effect)
    debug_snapshot = {'score': final_score, 'penalty': penalty}
    
    return final_score

# Main execution
sensor_data = [288.15, 295.65, 302.45, 278.2, 285.0, 305.1, 273.15, 281.2]
processed_data = analyze_temperatures(sensor_data)
final_score = calculate_final_score(processed_data)
print(f"Target result: {final_score}")