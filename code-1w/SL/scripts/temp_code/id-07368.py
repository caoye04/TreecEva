from collections import defaultdict, Counter

# Simulate sensor data with noise and redundant readings
def generate_noisy_data():
    raw_readings = [15, 18, 15, 22, 25, 18, 15, 30, 22, 18, 15, 25]
    timestamps = list(range(len(raw_readings)))
    sensor_log = [(t, r) for t, r in zip(timestamps, raw_readings)]
    return sensor_log

def analyze_trends(readings):
    trend_counter = defaultdict(int)
    for i in range(1, len(readings)):
        if readings[i] > readings[i-1]:
            trend_counter['increasing'] += 1
        elif readings[i] < readings[i-1]:
            trend_counter['decreasing'] += 1
        else:
            trend_counter['stable'] += 1
    return trend_counter

def filter_outliers(data, window=2):
    filtered = []
    for i in range(len(data)):
        neighbor_avg = 0
        count = 0
        for j in range(max(0, i - window), min(len(data), i + window + 1)):
            if i != j:
                neighbor_avg += data[j][1]
                count += 1
        if count > 0:
            neighbor_avg /= count
        if abs(data[i][1] - neighbor_avg) <= 10:
            filtered.append(data[i])
    return filtered

def calculate_consistency_score(events):
    event_counts = Counter(events)
    total = sum(event_counts.values())
    if total == 0:
        return 0.0
    entropy = 0.0
    for count in event_counts.values():
        p = count / total
        if p > 0:
            entropy -= p * (p).bit_length()  # Simplified pseudo-entropy
    return round(100 * (1 - entropy / 5), 3)

def calculate_final_score(log_entries, limit):
    values = [entry[1] for entry in log_entries]
    
    # Irrelevant aggregation: counts transitions but not used in final score
    temp_transition_count = 0
    for i in range(1, len(values)):
        if values[i] != values[i-1]:
            temp_transition_count += 1
    
    # Actual logic: count how many exceed threshold
    above_threshold = [v for v in values if v > limit]
    
    # Distractor: complex dictionary restructuring
    detailed_map = defaultdict(list)
    for t, v in log_entries:
        detailed_map[v].append(t)
    size_factor = len(detailed_map) * 2
    
    # Another distractor: unused trend analysis
    trends = analyze_trends(values)
    trend_bonus = 1 if trends['increasing'] > trends['decreasing'] else 0
    
    # Core scoring logic
    base_score = sum(above_threshold)
    penalty = len([v for v in values if v < 10])
    consistency_events = ['high' if v > limit else 'low' for v in values]
    consistency = calculate_consistency_score(consistency_events)
    
    # Final computation
    final_score = base_score - penalty * 5 + int(consistency) + size_factor
    return final_score

# Main execution
sensor_data = generate_noisy_data()
processed_data = filter_outliers(sensor_data, window=2)
threshold = 20
dummy_aggregation = sum(ts for ts, val in processed_data)  # Unused distraction
normalization_shift = max(val for ts, val in processed_data) / 100  # Unused
final_score = calculate_final_score(processed_data, threshold)
print(f"Result: {final_score}")