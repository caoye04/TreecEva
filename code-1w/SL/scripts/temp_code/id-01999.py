import math

# Simulate sensor data processing pipeline with noise filtering and efficiency calculation
def process_sensor_data(raw_readings):
    filtered_data = []
    noise_count = 0
    cumulative_signal = 0.0

    # Apply moving threshold filter to remove outliers
    for value in raw_readings:
        if abs(value - sum(filtered_data) / (len(filtered_data) or 1)) > 50 and len(filtered_data) > 0:
            noise_count += 1
            continue
        if value >= 0:
            filtered_data.append(value)

    # Misleading transformation: frequency modulation simulation (not used in final score)
    modulated = list(map(lambda x: (x * 1.05) % 360, [v + 10 for v in filtered_data if v < 80]))
    avg_modulation = sum(modulated) / (len(modulated) or 1)

    # Signal integrity check (semi-relevant - used in weighting)
    peak_value = max(filtered_data)
    base_floor = min(filtered_data)
    signal_span = peak_value - base_floor

    # Auxiliary calculation: harmonic distortion index (distraction)
    distortion_index = 0
    for i in range(1, len(filtered_data)):
        if filtered_data[i] > filtered_data[i-1]:
            distortion_index += math.sin(filtered_data[i] / 10)

    # Core efficiency metric computation
    valid_segments = 0
    segment_weights = []
    for i in range(0, len(filtered_data) - 2, 3):
        segment = filtered_data[i:i+3]
        if len(segment) == 3:
            segment_avg = sum(segment) / 3
            if segment_avg > base_floor + 0.3 * signal_span:
                valid_segments += 1
                segment_weights.append(segment_avg)

    # Efficiency score depends on weighted contribution of high-value segments
    total_weight = sum(segment_weights)
    expected_segments = len(filtered_data) // 3
    coverage_ratio = valid_segments / (expected_segments or 1)
    weight_factor = total_weight / (sum(filtered_data) or 1)

    # Final scoring formula
    raw_efficiency = (coverage_ratio * 100) + (weight_factor * 50)
    
    # Secondary adjustment based on data stability
    variance_proxy = sum((x - sum(filtered_data)/(len(filtered_data) or 1))**2 for x in filtered_data) / (len(filtered_data) or 1)
    stability_bonus = max(0, (10 - variance_proxy) / 10)
    
    efficiency_score = raw_efficiency + (stability_bonus * 15)
    
    # Tracking metrics
    final_metrics = []
    final_metrics.append(noise_count)          # distractor
    final_metrics.append(distortion_index)     # distractor
    final_metrics.append(avg_modulation)       # semi-relevant but unused
    final_metrics.append(efficiency_score)     # key assignment point
    
    # Print result as required
    print(f"Result: {efficiency_score}")
    
    return final_metrics

# Input data: simulated IoT sensor stream (temperature readings in tenths of °C)
raw_input = [235, 180, 250, 9999, -45, 240, 260, 75, 85, 270, 255, 265, 100, 90, 80, 200, 190]

# Execute
process_sensor_data(raw_input)