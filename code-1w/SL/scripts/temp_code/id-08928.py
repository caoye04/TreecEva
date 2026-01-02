from itertools import combinations
from math import log, sin

# Simulated sensor data processing with performance evaluation
raw_readings = [127, 255, 64, 192, 32, 160, 8, 80]

# Irrelevant transformation - red herring (bit manipulation)
decoys = [(x ^ 17) & 255 for x in raw_readings]
checksum = sum(decoys) % 1000

# Signal filtering: extract high-confidence signals
confidence_flags = [x > 100 for x in raw_readings]
valid_indices = [i for i, flag in enumerate(confidence_flags) if flag]
filtered_readings = [raw_readings[i] for i in valid_indices]

# Misleading statistical summary (not used in final result)
mean_reading = sum(filtered_readings) / len(filtered_readings) if filtered_readings else 0
variance_proxy = sum((x - mean_reading) ** 2 for x in filtered_readings) / len(filtered_readings) if filtered_readings else 0

# Frequency analysis of bit patterns (distraction)
bit_frequency = [0] * 8
for val in raw_readings:
    for bit in range(8):
        bit_frequency[bit] += (val >> bit) & 1

# Generate synthetic feature set using combinatorics (some features are decoys)
feature_pool = []
for r in range(2, 4):
    for combo in combinations(filtered_readings, r):
        feature_pool.append(sum(combo) / len(combo))

# Assign semantic labels to features (mostly irrelevant)
label_mapping = {i: f"FTR_{i}_{('HIGH' if v > 128 else 'LOW')}" for i, v in enumerate(feature_pool)}
high_value_features = [v for v in feature_pool if v > 100]

# Core metrics computation (only this part matters)
def compute_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count / total) * log(count / total) for count in counts.values())

entropy_metric = compute_entropy(raw_readings)
peak_to_avg_ratio = max(raw_readings) / mean_reading if mean_reading else 0
stability_index = sum(1 for x in confidence_flags if x) / len(confidence_flags)
signal_density = len(filtered_readings) / len(raw_readings)

# Weighted metric aggregation setup
metrics = {
    'entropy': entropy_metric,
    'p2a_ratio': peak_to_avg_ratio,
    'stability': stability_index,
    'density': signal_density
}

weights = {
    'entropy': 0.3,
    'p2a_ratio': 0.1,
    'stability': 0.4,
    'density': 0.2
}

# Decoy function - looks important but unused
def analyze_redundancy(data):
    redundant_pairs = 0
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if (data[i] & data[j]) == min(data[i], data[j]):
                redundant_pairs += 1
    return redundant_pairs / (len(data) * (len(data) - 1) / 2) if data else 0

# Another distraction: time-series-like windowing (unused)
window_size = 3
sliding_windows = [raw_readings[i:i+window_size] for i in range(len(raw_readings)-window_size+1)]
window_variances = [sum((x - sum(w)//len(w))**2 for x in w) for w in sliding_windows]

# Real evaluation logic buried among distractions
evaluate_performance = lambda m, w: sum(m[key] * w[key] for key in m if key in w)

# Key statement
final_score = evaluate_performance(metrics, weights)

# Output target result
print(f"Result: {final_score}")