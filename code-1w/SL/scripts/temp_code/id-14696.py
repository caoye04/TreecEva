from collections import defaultdict

# Simulate sensor data aggregation with noise filtering and weighted scoring
def collect_sensor_data():
    raw_data = [15, 23, 18, 27, 14, 21, 30, 12]
    filtered = [x for x in raw_data if x >= 15]
    temp_offset = 5
    adjusted = [x + temp_offset for x in filtered]  # Simulated calibration
    return adjusted

# Analyze frequency of readings above threshold
def analyze_distribution(data):
    freq = defaultdict(int)
    for val in data:
        freq[val // 10] += 1
    high_range_count = sum(freq[k] for k in freq if k >= 2)
    mid_weight = 0.7
    return high_range_count * mid_weight

# Apply dynamic weight adjustments based on distribution skew
def adjust_weights(base_weights, skew_factor):
    adjusted = {}
    for k, v in base_weights.items():
        if k == 'primary':
            adjusted[k] = v * (1 + skew_factor / 10)
        else:
            adjusted[k] = v
    scale_factor = 1.0 / sum(adjusted.values())
    return {k: v * scale_factor for k, v in adjusted.items()}

# Main scoring logic combining multiple metrics
def calculate_final_score(data, weights):
    avg_val = sum(data) / len(data)
    peak_val = max(data)
    stability_score = sum(1 for i in range(1, len(data)) if abs(data[i] - data[i-1]) < 10)
    
    # Irrelevant intermediate calculation (distractor)
    outlier_check = [x for x in data if x > 35]
    anomaly_flag = len(outlier_check) > 0
    
    base_component = avg_val * weights['primary']
    secondary_component = peak_val * 0.3
    tertiary_component = stability_score * weights.get('tertiary', 0.2)
    
    # Unused branch (dead code - mild interference)
    if anomaly_flag:
        secondary_component *= 0.9  # Never reached
    
    total = base_component + secondary_component + tertiary_component
    
    # Final normalization step
    normalized = int(total) + (stability_score % 3)
    return normalized

# --- Execution Flow ---
data_samples = collect_sensor_data()
distribution_skew = analyze_distribution(data_samples)

base_weights = {
    'primary': 0.6,
    'secondary': 0.3,
    'tertiary': 0.1
}

final_weights = adjust_weights(base_weights, distribution_skew)

# Key statement
final_score = calculate_final_score(data_samples, final_weights)

# Debugging variables (not used in final result)
copy_of_data = data_samples[:]
duplicate_calc = sum(copy_of_data) / len(copy_of_data)

# Output result
print(f"Result: {final_score}")