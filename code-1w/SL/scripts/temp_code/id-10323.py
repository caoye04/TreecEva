from collections import defaultdict
import math

# Simulate sensor data aggregation and performance scoring
def collect_sensor_readings():
    readings = [12, 15, 22, 8, 19, 34, 27, 11]
    offset = 5
    adjusted = [r + offset for r in readings]  # Distractor: not used later
    return readings

def compute_moving_average(data, window=3):
    averages = []
    for i in range(len(data) - window + 1):
        averages.append(sum(data[i:i+window]) / window)
    padding = [None] * (window // 2)  # Irrelevant padded structure
    return padding + averages + padding

def analyze_trend_pattern(seq):
    trend_flags = []
    for i in range(1, len(seq)):
        if seq[i] > seq[i-1]:
            trend_flags.append(1)
        elif seq[i] < seq[i-1]:
            trend_flags.append(-1)
        else:
            trend_flags.append(0)
    upturns = sum(1 for x in trend_flags if x == 1)
    downturns = sum(1 for x in trend_flags if x == -1)
    net_bias = upturns - downturns  # Semi-relevant but not directly used
    return trend_flags

def calculate_entropy(values):
    freq = defaultdict(int)
    for v in values:
        freq[v] += 1
    total = len(values)
    entropy = 0.0
    for count in freq.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def apply_correction_factor(x, method='xor'):
    if method == 'xor':
        return x ^ 7  # Bitwise operation
    elif method == 'add':
        return x + 3
    return x  # Dead code path fallback

def evaluate_performance(weights, data):
    avg_val = sum(data) / len(data)
    ent = calculate_entropy(data)
    
    # Misleading intermediate calculations
    temp_snapshot = {'mean': avg_val, 'entropy': ent}
    snapshot_hash = apply_correction_factor(int(avg_val), 'xor')
    
    # Core logic masked with noise
    weight_sum = sum(weights.values())
    adjusted_entropy = ent * 10
    raw_score = avg_val + adjusted_entropy
    
    # Key interference: irrelevant conditional block
    if len(data) % 2 == 0:
        dummy_var = [x ** 0.5 for x in data if x > 10]
        _ = sum(dummy_var) / len(dummy_var) if dummy_var else 0

    # Actual score computation
    scaling_factor = 1.75
    final_score = int(raw_score * scaling_factor)
    
    # Red herring: unused transformation chain
    transformed = [apply_correction_factor(x, 'xor') for x in data]
    _ = compute_moving_average(transformed)  # Computed but ignored

    return final_score

# Main execution flow
raw_data = collect_sensor_readings()
metric_weights = {'stability': 0.4, 'response_time': 0.6}
final_score = evaluate_performance(metric_weights, raw_data)
print(f"Result: {final_score}")