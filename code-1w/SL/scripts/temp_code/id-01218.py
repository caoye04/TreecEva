from collections import defaultdict, Counter
import math

def analyze_trends(data, threshold=0.5):
    trends = []
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            trends.append('up')
        elif data[i-1] - data[i] > threshold:
            trends.append('down')
        else:
            trends.append('stable')
    return trends

def compute_moving_average(series, window=3):
    smoothed = []
    for i in range(len(series)):
        start = max(0, i - window + 1)
        smoothed.append(sum(series[start:i+1]) / (i - start + 1))
    return smoothed

def simulate_failure_modes(inputs):
    # Irrelevant simulation function (dead code path)
    critical_faults = 0
    for val in inputs:
        if val < 0:
            critical_faults += 1
    return critical_faults

def preprocess_signal(raw_readings):
    # Distractor: signal processing that isn't used later
    filtered = [x * 0.95 for x in raw_readings if x > 0]
    envelope = max(filtered) - min(filtered) if filtered else 0
    return [x / envelope for x in filtered] if envelope else filtered

def calculate_entropy(values):
    counts = Counter(values)
    total = len(values)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * math.log2(p)
    return round(entropy, 6)

def normalize_vector(vec):
    norm = math.sqrt(sum(x ** 2 for x in vec))
    return [x / norm for x in vec] if norm != 0 else vec

def generate_combinations(items):
    # Unused combinatorics (red herring)
    combos = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            combos.append((items[i], items[j]))
    return combos

def detect_outliers(sequence, std_devs=2):
    mean_val = sum(sequence) / len(sequence)
    variance = sum((x - mean_val) ** 2 for x in sequence) / len(sequence)
    std_dev = math.sqrt(variance)
    return [x for x in sequence if abs(x - mean_val) > std_devs * std_dev]

def rank_elements(arr):
    sorted_with_idx = sorted([(arr[i], i) for i in range(len(arr))], reverse=True)
    ranks = [0] * len(arr)
    for rank, (_, idx) in enumerate(sorted_with_idx):
        ranks[idx] = rank + 1
    return ranks

def evaluate_performance(weights, data_points):
    weighted_sum = 0.0
    for w, d in zip(weights, data_points):
        weighted_sum += w * d
    penalty = 0.0
    if len(data_points) > 5:
        penalty = (len(data_points) - 5) * 0.1
    return int((weighted_sum - penalty) * 100)

# Main execution flow
raw_metrics = [0.82, 0.76, 0.91, 0.64, 0.88, 0.73]
metric_names = ['latency', 'throughput', 'accuracy', 'reliability', 'availability', 'scalability']

# Irrelevant data structures and transformations
metric_dict = defaultdict(float)
for name, val in zip(metric_names, raw_metrics):
    metric_dict[name] = val

# Simulate some unused analysis
outlier_check = detect_outliers(raw_metrics)
signal_input = [-0.2, 0.1, 0.5, 0.9, 0.0, 0.3]
processed_signal = preprocess_signal(signal_input)

trend_analysis = analyze_trends(raw_metrics)
entropy_value = calculate_entropy(trend_analysis)

# Core relevant computation begins here
base_weights = [3, 2, 4, 1, 3, 2]
adjusted_weights = normalize_vector(base_weights)

smoothed_metrics = compute_moving_average(raw_metrics, window=2)
ranked_positions = rank_elements(smoothed_metrics)

# Normalize metrics to [0,1] range
normalized_data = [min(max(m, 0), 1) for m in smoothed_metrics]

# Introduce decoy combination logic
all_pairs = generate_combinations(normalized_data)

# Key statement with actual answer computation
final_score = evaluate_performance(adjusted_weights, normalized_data)

# Print result as required
print(f"Target result: {final_score}")