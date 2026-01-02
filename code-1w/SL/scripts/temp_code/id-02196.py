import itertools

# Simulated sensor data processing with performance evaluation
def analyze_readings(readings):
    filtered = [x for x in readings if 10 < x < 90]
    smoothed = [sum(readings[i:i+3]) / 3 for i in range(len(readings) - 2)]
    anomalies = [i for i, v in enumerate(smoothed) if v > 75]
    return filtered, smoothed, anomalies

def calculate_entropy(data):
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    entropy = 0
    for count in counts.values():
        p = count / total
        entropy -= p * __import__('math').log2(p) if p > 0 else 0
    return round(entropy, 6)

def bitwise_transform(n):
    # Irrelevant transformation used as distractor
    return (n ^ 242) >> 2 | (n << 1) & 255

def legacy_validation(seq):
    # Dead code path - never actually used in main logic
    if len(seq) < 5:
        return False
    checksum = 0
    for i, val in enumerate(seq):
        checksum ^= (val + i) % 17
    return checksum == 12

def generate_combinations(values):
    # Distractor: generates unused combinations
    return list(itertools.combinations(values, 3))

def rolling_window_stats(data, window_size=4):
    # Unused advanced stat computation
    stats = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        mean = sum(window) / len(window)
        variance = sum((x - mean) ** 2 for x in window) / len(window)
        stats.append((mean, variance))
    return stats

def extract_patterns(sequence):
    # Real but indirectly used function
    patterns = {}
    for i in range(len(sequence) - 1):
        pair = (sequence[i], sequence[i+1])
        patterns[pair] = patterns.get(pair, 0) + 1
    return patterns

def evaluate_monotonicity(arr):
    # Misleading intermediate metric
    increasing = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    decreasing = all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
    return int(increasing) - int(decreasing)

def count_transitions(data, threshold=50):
    # Counts crossings over threshold - relevant later
    transitions = 0
    for i in range(1, len(data)):
        if (data[i-1] <= threshold) != (data[i] <= threshold):
            transitions += 1
    return transitions

def compute_fractal_dimension(series):
    # Decoy scientific calculation - not actually needed
    n = len(series)
    if n < 2:
        return 0.0
    diffs = [abs(series[i+1] - series[i]) for i in range(n-1)]
    total_length = sum(diffs)
    if total_length == 0:
        return 1.0
    straight_line = max(series) - min(series)
    return round(total_length / (straight_line + 1e-8), 6)

def evaluate_performance(metrics, base_threshold):
    # Core logic hidden among distractions
    raw_values = [v["value"] for v in metrics if v["active"]]
    
    # Key preprocessing step
    processed = [x for x in raw_values if isinstance(x, (int, float)) and x >= 0]
    
    # Extract key feature: transition count around base_threshold
    t_count = count_transitions(processed, base_threshold)
    
    # Another relevant transform
    pattern_map = extract_patterns(processed)
    pattern_bonus = len([k for k, v in pattern_map.items() if v >= 2]) * 3
    
    # Main scoring logic
    base_score = sum(processed) // len(processed) if processed else 0
    adjustment = t_count * 7
    penalty = len([x for x in processed if x > 85]) * 4
    
    # Final combination
    final_score = base_score + adjustment - penalty + pattern_bonus
    
    # Red herring: bitwise operation on score that isn't used
    obfuscated = bitwise_transform(final_score)
    
    return final_score  # This is what we actually need

# Simulated input data
sensor_data = [12, 15, 23, 45, 67, 78, 89, 76, 65, 58, 52, 48, 39, 28, 19, 14, 22, 38, 55, 61]

# Generate irrelevant outputs to distract
filtered_data, moving_avg, anomaly_indices = analyze_readings(sensor_data)
dummy_combos = generate_combinations(moving_avg[:6])
legacy_flag = legacy_validation(anomaly_indices)
window_stats = rolling_window_stats(sensor_data, 3)
entropy_val = calculate_entropy([int(x) for x in moving_avg])
fractal_dim = compute_fractal_dimension(moving_avg)
monotonic_result = evaluate_monotonicity(filtered_data)

data_metrics = [
    {"value": sensor_data[i], "active": i % 3 != 2} for i in range(len(sensor_data))
]

base_threshold = 40

# Critical execution point
final_score = evaluate_performance(data_metrics, base_threshold)

print(f"Result: {final_score}")