from collections import defaultdict
import math

def preprocess_data(raw):
    # Irrelevant preprocessing steps with red herrings
    temp_map = defaultdict(int)
    for k, v in raw.items():
        if v % 3 == 0:
            temp_map[k] += v * 2
        elif v % 5 == 0:
            temp_map[k] += v // 2
        else:
            temp_map[k] += v
    adjustment = sum(temp_map.values()) % 7
    return dict(temp_map), adjustment

def validate_checksum(arr):
    # Dead function - never used but looks important
    chk = 0
    for i, val in enumerate(arr):
        chk ^= (val + i) * 3
    return chk % 100 == 42

def transform_signal(signal):
    # Distractor computation - looks critical but unused
    transformed = []
    for x in signal:
        transformed.append(int(math.sin(x) * 100))
    return [t for t in transformed if t != 0]

def filter_outliers(data_dict, threshold=50):
    # Seemingly relevant filtering, partially used but not on main path
    cleaned = {}
    outlier_log = []
    for k, v in data_dict.items():
        if abs(v) > threshold:
            outlier_log.append(k)
        else:
            cleaned[k] = v
    # Log ignored
    return cleaned  # Used in a limited way

def accumulate_weighted_sum(values, multipliers):
    # Core logic buried in noise
    total = 0.0
    keys = sorted(values.keys())
    for k in keys:
        if k in multipliers:
            total += values[k] * multipliers[k]
    return total

def derive_key_factor(x):
    # Misleading helper with complex math
    if x <= 0:
        return 0.1
    return math.log(x + 1) / (x ** 0.5)

def calculate_entropy(distribution):
    # Completely irrelevant function - distractor
    entropy = 0.0
    total = sum(distribution)
    for val in distribution:
        p = val / total
        if p > 0:
            entropy -= p * math.log2(p)
    return round(entropy, 4)

def calculate_final_score(dataset, config):
    # Main logic hidden among distractions
    base_data, adj = preprocess_data(dataset)
    
    # Red herring: complex conditional that evaluates but doesn't affect outcome
    if adj > 4:
        scale = 1.2
    else:
        scale = 0.95
    
    # Real operation: filter first
    filtered_data = filter_outliers(base_data, threshold=200)
    
    # More distraction: signal transformation on unrelated data
    dummy_signal = [1, 5, 10, 15, 20]
    processed_signal = transform_signal(dummy_signal)
    
    # Key computation - weighted accumulation
    raw_sum = accumulate_weighted_sum(filtered_data, config)
    
    # Fake normalization path
    peak = max(filtered_data.values()) if filtered_data else 1
    normalized_sum = raw_sum / peak if peak > 0 else 0
    
    # Decoy entropy calculation
    decoy_dist = [abs(v) for v in filtered_data.values() if v > 0]
    _ = calculate_entropy(decoy_dist) if decoy_dist else 0.0
    
    # Final score depends only on raw_sum and a hidden constant from config
    bonus = config.get('bonus', 0)
    final_score = int(raw_sum + bonus * 2.5)
    
    return final_score

# Simulated input data with meaningful names
network_metrics = {
    'latency': 42,
    'throughput': 180,
    'retries': 6,
    'timeout_count': 15,
    'packet_loss': 3
}

# Weight configuration with red herring entries
weights = {
    'latency': 0.8,
    'throughput': 1.5,
    'retries': -2.0,
    'timeout_count': -1.0,
    'jitter': 3.0,  # Not in data - irrelevant
    'bonus': 10     # Hidden bonus key
}

# Execution point of interest
final_score = calculate_final_score(network_metrics, weights)

print(f"Result: {final_score}")