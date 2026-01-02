from collections import defaultdict
from itertools import combinations

# Simulate sensor data with noise and redundancy
def process_sensor_readings(raw_data):
    filtered = [x for x in raw_data if x > 0]
    temp_stats = defaultdict(int)
    
    for val in filtered:
        if val % 2 == 0:
            temp_stats['even'] += 1
        else:
            temp_stats['odd'] += 1
    
    # Distractor: unused statistical placeholder
    temp_stats['mean'] = sum(filtered) / len(filtered) if filtered else 0
    
    return temp_stats, len(filtered)

# Analyze correlation between paired sensors
def detect_anomalies(pairs):
    anomalies = 0
    for a, b in pairs:
        if abs(a - b) > 3:
            anomalies += 1
    return anomalies

# Main processing pipeline
raw_input = [1, 4, 2, 0, 5, 6, -1, 3, 8, 7]

# Step 1: Filter and analyze basic stats
stats, valid_count = process_sensor_readings(raw_input)

# Step 2: Generate all possible pairs (including irrelevant ones)
all_pairs = list(combinations([x for x in raw_input if x > 0], 2))
anomaly_count = detect_anomalies(all_pairs)

# Step 3: Compute weighted signal integrity index
signal_weights = []
for x in raw_input:
    if x > 5:
        signal_weights.append(x * 0.8)
    elif x > 2:
        signal_weights.append(x * 0.5)
    else:
        signal_weights.append(x * 0.3)

# Distractor: calculate but don't fully use
average_weight = sum(signal_weights) / len(signal_weights) if signal_weights else 0

# Step 4: Aggregate final evaluation score
base_score = stats['even'] * 10
penalty = anomaly_count * 2
bonus = 5 if stats['odd'] > stats['even'] else 0

# Critical computation point
final_score = base_score - penalty + bonus + int(average_weight)

print(f"Result: {final_score}")