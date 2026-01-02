from collections import defaultdict

# Simulate sensor data readings over time with some noise
def generate_sensor_data():
    return [105, 98, 110, 102, 95, 108, 100, 103, 97, 101]

# Analyze trends in sensor values
def analyze_trend(data):
    increasing = decreasing = stable = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            increasing += 1
        elif data[i] < data[i-1]:
            decreasing += 1
        else:
            stable += 1
    return increasing, decreasing, stable

# Evaluate system performance based on adjusted thresholds
def evaluate_performance(raw_data, baseline=100):
    adjustments = []
    temp_offset = 0
    for val in raw_data:
        if val > baseline + 5:
            temp_offset += 0.5
        elif val < baseline - 5:
            temp_offset -= 0.3
        adjustments.append(temp_offset)
    
    # Apply smoothing using slicing to avoid edge spikes
    smoothed = [raw_data[i] + adjustments[i] for i in range(len(raw_data))]
    trimmed = smoothed[1:-1]  # Remove first and last to reduce outlier impact
    
    # Compute moving average of three elements where possible
    moving_averages = []
    for i in range(len(trimmed) - 2):
        avg = (trimmed[i] + trimmed[i+1] + trimmed[i+2]) / 3
        moving_averages.append(avg)
    
    # Count how many are above threshold
    threshold_count = 0
    for m in moving_averages:
        if m > baseline:
            threshold_count += 1
    
    # Irrelevant distraction: log unused stats
    debug_stats = defaultdict(int)
    for x in moving_averages:
        if x > 102:
            debug_stats['high'] += 1
        elif x < 98:
            debug_stats['low'] += 1
        else:
            debug_stats['normal'] += 1
    
    # Dummy calculation that does nothing
    dummy_sum = sum([i**2 for i in range(5)]) * 0.01  # Serves no purpose
    
    # Final score based on count above baseline
    final_score = threshold_count * 10
    
    # Additional red herring: modify score with unrelated logic
    penalty = 0
    for i, val in enumerate(raw_data):
        if i % 3 == 0 and val < 100:
            penalty += 2
    final_score -= penalty  # This affects result but is non-obvious
    
    return final_score

# Main execution
sensor_readings = generate_sensor_data()
trend_analysis = analyze_trend(sensor_readings)

# Key computation point
final_score = evaluate_performance(sensor_readings)

print(f"Result: {final_score}")