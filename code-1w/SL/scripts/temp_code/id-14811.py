from collections import defaultdict

# Simulate sensor data over time with some noise
def generate_sensor_readings():
    readings = []
    for t in range(10):
        base_value = (t * 2.5) + (t % 3)
        noisy_value = base_value + (0.1 * t)
        readings.append(noisy_value)
    return readings

# Misleading auxiliary function that computes irrelevant statistics
def analyze_trend(data):
    trend_changes = 0
    for i in range(1, len(data)):
        if (data[i] - data[i-1]) * (data[i-1] - data[i-2]) < 0 if i > 1 else False:
            trend_changes += 1
    return trend_changes  # Not used in final result

# Core processing: filter anomalies and compute performance metric
def calculate_performance(raw_data):
    filtered = [x for x in raw_data if 5 <= x <= 20]  # Only valid range
    
    # Track frequency of rounded values
    freq_map = defaultdict(int)
    for val in filtered:
        freq_map[round(val)] += 1
    
    # Compute weighted score based on position and frequency
    positional_sum = 0
    for idx, val in enumerate(filtered):
        positional_sum += val * (idx + 1)
    
    average_positional = positional_sum / len(filtered) if filtered else 0
    
    # Secondary metric (distractor)
    peak_count = sum(1 for i in range(1, len(filtered)-1) 
                     if filtered[i] > filtered[i-1] and filtered[i] > filtered[i+1])
    
    # Final computation
    unique_contributions = len(set(round(x) for x in filtered))
    final_score = int(average_positional + unique_contributions)
    
    return final_score

# Main execution
sensor_data = generate_sensor_readings()
baseline_shift = sum(x for x in sensor_data if x < 3)  # Irrelevant baseline
noise_floor = max(sensor_data) - min(sensor_data)  # Red herring metric

# Key statement
final_score = calculate_performance(sensor_data)

print(f"Result: {final_score}")