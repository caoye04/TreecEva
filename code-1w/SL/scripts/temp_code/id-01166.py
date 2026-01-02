def analyze_trends(data_slice):
    trend_sum = 0
    fluctuations = 0
    for i in range(1, len(data_slice)):
        diff = data_slice[i] - data_slice[i-1]
        if diff > 0:
            trend_sum += diff
        else:
            fluctuations += abs(diff)
    return trend_sum, fluctuations


def filter_outliers(raw_values):
    if len(raw_values) < 3:
        return raw_values
    sorted_vals = sorted(raw_values)
    trimmed = sorted_vals[1:-1]  # Remove min and max
    return trimmed


def calculate_final_score(input_array):
    # Irrelevant preprocessing (distractor)
    temp_buffer = [x * 1.1 for x in input_array if x > 0]
    avg_temp = sum(temp_buffer) / len(temp_buffer) if temp_buffer else 0
    
    # Actual relevant processing
    safe_data = filter_outliers(input_array)
    baseline = sum(safe_data) / len(safe_data)
    
    # Slice for trend analysis
    recent_segment = safe_data[-5:] if len(safe_data) >= 5 else safe_data[:]
    growth, noise = analyze_trends(recent_segment)
    
    # Dummy computations (misleading)
    peak_value = max(input_array) if input_array else 0
    normalized_peak = peak_value / (baseline + 1e-5)
    
    # Core logic
    stability_factor = len(safe_data) / len(input_array) if input_array else 0
    signal_quality = growth - noise
    
    # Final score calculation (key step)
    final_score = int((baseline * stability_factor) + signal_quality)
    
    # Dead code path (red herring)
    if False:
        correction_term = avg_temp - normalized_peak
        final_score -= int(correction_term)
        
    return final_score

# Main execution
raw_input = [12, -5, 8, 14, 9, 11, 13, 7, 10]
discarded_portion = raw_input[::2]
processed_data = raw_input.copy()

# Key statement
final_score = calculate_final_score(processed_data)
print(f"Result: {final_score}")