from collections import defaultdict, Counter

# Simulate sensor data with noise and valid readings
def generate_sensor_readings():
    raw_data = [102, 98, None, 105, 103, None, 97, 100, 101, 104]
    timestamps = list(range(len(raw_data)))
    return list(zip(timestamps, raw_data))

def analyze_trend(readings):
    trend_values = []
    for i in range(1, len(readings)):
        prev = readings[i-1][1]
        curr = readings[i][1]
        if prev is not None and curr is not None:
            trend_values.append(curr - prev)
    return trend_values

def calculate_noise_level(data):
    # Irrelevant helper function - included as distraction
    counter = Counter()
    for _, val in data:
        if val is not None:
            bucket = val // 5
            counter[bucket] += 1
    return sum(counter.values()) // len(counter) if counter else 0

def calculate_performance(log_entries):
    # Extract only valid sensor values
    valid_entries = [val for _, val in log_entries if val is not None]
    
    # Track frequency of each reading (semi-relevant)
    freq_map = defaultdict(int)
    for v in valid_entries:
        freq_map[v] += 1
    
    # Compute rolling average of last 3 points (distraction)
    rolling_avg = 0
    if len(valid_entries) >= 3:
        rolling_avg = sum(valid_entries[-3:]) / 3
    
    # Core logic: stability score based on absolute differences
    stability_score = 0
    for i in range(1, len(valid_entries)):
        stability_score += abs(valid_entries[i] - valid_entries[i-1])
    
    # Normalize and invert for performance (higher = more stable)
    max_possible_drift = 10 * (len(valid_entries) - 1)  # Assume max change per step is 10
    normalized_drift = stability_score / max_possible_drift if max_possible_drift > 0 else 0
    performance_ratio = 1 - normalized_drift
    
    # Apply non-linear boost
    boosted_score = int(1000 * (performance_ratio ** 2))
    
    # Distractor computation: use of list comprehension with unused result
    outliers = [v for v in valid_entries if abs(v - 100) > 5]
    outlier_impact = len(outliers) * 2
    
    # Final adjustment based on data completeness
    completeness = len([v for _, v in log_entries if v is not None])
    completeness_bonus = (completeness / len(log_entries)) * 100
    
    # Final score calculation
    final_score = boosted_score + completeness_bonus - outlier_impact
    
    # Irrelevant print for distraction
    debug_info = f'Readings: {valid_entries}, Outliers: {outliers}'
    
    return int(final_score)

# Main execution flow
sensor_log = generate_sensor_readings()
trends = analyze_trend(sensor_log)
noise = calculate_noise_level(sensor_log)
final_score = calculate_performance(sensor_log)
print(f"Result: {final_score}")