import itertools

# Simulated sensor metrics from a distributed system (some are decoys)
sensor_a_readings = [0.8, 0.9, 0.75, 0.88]
sensor_b_readings = [0.6, 0.65, 0.7, 0.55]
sensor_c_readings = [0.95, 0.99, 0.93, 0.97]  # irrelevant
temperature_logs = [23.5, 24.1, 22.9, 25.0]  # completely irrelevant

# System health indicators (only some used)
latency_ms = [120, 140, 110, 130]
packet_loss = [0.01, 0.02, 0.005, 0.015]
throughput_mbps = [85, 80, 90, 87]
retries_count = [2, 3, 1, 4]  # unused

def moving_average(data, window=2):
    """Irrelevant helper function for smoothing data."""
    result = []
    for i in range(len(data) - window + 1):
        result.append(sum(data[i:i+window]) / window)
    return result

def normalize(values):
    """Normalize values to 0-1 range using min-max scaling."""
    min_val, max_val = min(values), max(values)
    return [(v - min_val) / (max_val - min_val) for v in values]

def xor_cipher(data, key=42):
    """Misleading cryptographic transformation (unused)."""
    return [d ^ key for d in data]

def calculate_entropy(data):
    """Unused advanced metric."""
    from math import log2
    total = sum(data)
    if total == 0: return 0.0
    probs = [x / total for x in data]
    return -sum(p * log2(p) for p in probs if p > 0)

def extract_trend(signal):
    """Detect rising/falling trend as boolean array."""
    return [signal[i+1] > signal[i] for i in range(len(signal)-1)]

def weighted_sum(values, weights):
    """Compute weighted sum of aligned values."""
    return sum(v * w for v, w in zip(values, weights))

def filter_outliers(data, threshold=1.5):
    """Remove outliers based on IQR method (unused)."""
    sorted_data = sorted(data)
    q1, q3 = sorted_data[len(sorted_data)//4], sorted_data[3*len(sorted_data)//4]
    iqr = q3 - q1
    lower, upper = q1 - threshold * iqr, q3 + threshold * iqr
    return [x for x in data if lower <= x <= upper]

# Real processing begins here — but hidden among distractions
base_metrics = [
    sum(latency_ms) / len(latency_ms),  # avg_latency
    sum(packet_loss) / len(packet_loss), # avg_loss
    sum(throughput_mbps) / len(throughput_mbps) # avg_throughput
]

# Normalize each base metric (inverse for latency and loss)
normalized_metrics = [
    1 - normalize([base_metrics[0]])[0],  # better if lower
    1 - normalize([base_metrics[1]])[0],  # better if lower
    normalize([base_metrics[2]])[0]       # better if higher
]

# Decoy combinatorics: all possible 2-sensor pairs (irrelevant)
sensor_pairs = list(itertools.combinations(['A', 'B', 'C'], 2))
pair_analysis = {}
for pair in sensor_pairs:
    pair_analysis[pair] = {
        'correlation': 0.0,  # placeholder
        'phase_diff': None   # never used
    }

# More red herring: generate Cartesian product of trends (dead code path)
trend_combinations = list(itertools.product(
    extract_trend(sensor_a_readings),
    extract_trend(sensor_b_readings)
))
complex_flag = any(trend_combinations[i][0] and not trend_combinations[i][1] 
                   for i in range(0, len(trend_combinations), 2))

# Weights for final evaluation (only this matters now)
weights = [0.4, 0.3, 0.3]  # latency, loss, throughput

# Critical computation buried in noise
adjusted_metrics = [
    max(0.0, min(1.0, m)) for m in normalized_metrics  # clamp to [0,1]
]

# This function appears complex due to context but does direct calculation
def evaluate_performance(metrics, weights):
    score = weighted_sum(metrics, weights)
    # Apply non-linear boost if all metrics above threshold
    if all(m > 0.6 for m in metrics):
        score *= 1.25
    return int(score * 1000)  # scale to integer

# Final answer computed here
final_score = evaluate_performance(adjusted_metrics, weights)

# Irrelevant bit manipulation distraction
deco_result = 0
for i in range(8):
    deco_result ^= (final_score >> i) & 1

timestamp_groups = list(itertools.groupby([1, 1, 2, 2, 3], lambda x: x))  # unused

# Output the target result
print(f"Result: {final_score}")