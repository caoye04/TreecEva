from collections import defaultdict
import itertools

# Simulate sensor data analysis with noise filtering and metric aggregation
def analyze_readings(raw_data):
    filtered = [x for x in raw_data if 10 <= x <= 100]
    avg = sum(filtered) / len(filtered) if filtered else 0
    deviations = [abs(x - avg) for x in filtered]
    threshold = avg * 0.25
    anomalies = [x for x in filtered if abs(x - avg) > threshold]
    return anomalies, avg

# Generate synthetic data stream
data_stream = [12, 95, 15, 88, 20, 30, 75, 40, 60, 18, 90, 25, 35, 50, 45]

# Extract anomalies and average
anomalies, mean_val = analyze_readings(data_stream)

# Initialize various metrics (some are red herrings)
base_metrics = {}
base_metrics['count'] = len(data_stream)
base_metrics['valid_count'] = len([x for x in data_stream if x >= 10])
base_metrics['peak'] = max(data_stream) if data_stream else 0
base_metrics['noise_ratio'] = (len(data_stream) - len([x for x in data_stream if 10 <= x <= 100])) / len(data_stream)

# Secondary processing: group consecutive similar values
consecutive_groups = []
current_group = []
for val in data_stream:
    if current_group and abs(val - current_group[-1]) <= 5:
        current_group.append(val)
    else:
        if current_group:
            consecutive_groups.append(current_group)
        current_group = [val]
if current_group:
    consecutive_groups.append(current_group)

group_averages = [sum(g)/len(g) for g in consecutive_groups if len(g) > 1]

temp_offset = sum(group_averages) * 0.1  # Distractor computation
scaling_factor = 1.0 + (temp_offset / 100)  # Not actually used later

# Evaluate performance based on anomaly characteristics and base metrics
def evaluate_performance(anomalies, metrics):
    score = 0
    
    # Core logic: score increases with higher anomalies that are above mean
    anomaly_bonus = sum(a for a in anomalies if a > metrics['peak'] * 0.8)
    
    # Penalty for excessive anomalies
    if len(anomalies) > 3:
        score -= len(anomalies) * 5
    else:
        score += 20
    
    # Bonus for having at least one high-value anomaly
    if any(a > 90 for a in anomalies):
        score += 15
    
    # Irrelevant mapping (distractor)
    detail_map = defaultdict(int)
    for a in anomalies:
        detail_map[f'level_{a//10}'] += 1
    
    # More distractors: combinatorial pairing that doesn't affect result
    pseudo_pairs = list(itertools.combinations_with_replacement(anomalies, 2))
    dummy_sum = sum((p[0] * p[1]) % 7 for p in pseudo_pairs if p[0] != p[1])
    
    # Final scoring uses only specific components
    score += int(anomaly_bonus / 5)
    
    # Hidden adjustment: reduce score by number of distinct anomaly groups modulo 4
    grouped_anomalies = [a for a in anomalies if a < mean_val]
    adjustment = len(set(grouped_anomalies)) % 4
    score -= adjustment
    
    return score

# Critical execution point
final_score = evaluate_performance(anomalies, base_metrics)

print(f"Result: {final_score}")