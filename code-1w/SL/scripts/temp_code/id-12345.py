from itertools import compress, cycle
import math

def analyze_response_time(rt):
    # Irrelevant function: analyzes response time but not used in final calculation
    if rt < 0.1:
        return 'exceptional'
    elif rt < 0.5:
        return 'good'
    else:
        return 'slow'

def compute_entropy(data):
    # Dead code path — never called
    from collections import Counter
    counts = Counter(data)
    total = len(data)
    return -sum((count / total) * math.log2(count / total) for count in counts.values())

def evaluate_stability(readings):
    # Distractor function: calculates variance but isn't directly used
    mean = sum(readings) / len(readings)
    variance = sum((x - mean) ** 2 for x in readings) / len(readings)
    return variance < 5

def extract_signals(raw_logs):
    # Processes logs but only some output matters
    cleaned = []
    for log in raw_logs:
        parts = log.split(',')
        code = int(parts[1])
        timestamp = float(parts[2])
        if code == 200:
            cleaned.append(timestamp)
    return cleaned

def filter_anomalies(data, threshold=100):
    # Misleading intermediate: filters values above threshold
    return [x for x in data if x <= threshold]

def generate_weight_vector(n):
    # Creates a cyclic weight pattern — actually used
    gen = cycle([0.8, 1.2, 1.0])
    return [next(gen) for _ in range(n)]

def aggregate_performance(metrics, weights):
    # Core logic: weighted harmonic mean with filtering
    filtered_pairs = [(m, w) for m, w in zip(metrics, weights) if m > 0]
    weighted_inv = sum(w / m for m, w in filtered_pairs)
    total_weight = sum(w for m, w in filtered_pairs)
    return round(total_weight / weighted_inv, 6) if weighted_inv != 0 else 0

# Simulated system performance metrics (some are red herrings)
signal_strengths = [95, 87, 92, 88, 105, 89, 94]  # 105 is outlier
temp_readings = [23.5, 24.1, 23.9, 24.0, 25.2]  # Used to calculate fake stability flag
raw_network_logs = [
    "node1,200,12.1",
    "node2,500,12.3",
    "node3,200,12.5",
    "node4,404,12.6"
]

# Dead variable assignments (distractors)
baseline_latency = 0.23
peak_load = 1200
critical_threshold = 90
response_categories = {'fast': [], 'moderate': [], 'slow': []}

# Real pipeline begins here
filtered_metrics = filter_anomalies(signal_strengths, threshold=100)  # Removes 105
stability_flag = evaluate_stability(temp_readings)  # Returns True, not used later

# Extract useful timestamps (only for 200 codes)
heartbeat_intervals = extract_signals(raw_network_logs)  # Yields [12.1, 12.5]
interval_diffs = [heartbeat_intervals[i+1] - heartbeat_intervals[i] for i in range(len(heartbeat_intervals)-1)]

# These variables look important but aren't used in final score
anomaly_count = len(signal_strengths) - len(filtered_metrics)
dynamic_factor = math.sin(len(heartbeat_intervals))

# Build actual inputs for aggregation
base_metrics = [x / 10 for x in filtered_metrics]  # [9.5, 8.7, 9.2, 8.8, 8.9, 9.4]
weights = generate_weight_vector(len(base_metrics))  # [0.8, 1.2, 1.0, 0.8, 1.2, 1.0]

# Final computation
final_score = aggregate_performance(base_metrics, weights)

# Output result as required
print(f"Target result: {final_score}")