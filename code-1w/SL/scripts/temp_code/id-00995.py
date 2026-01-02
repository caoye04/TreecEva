def analyze_response_time(raw_logs):
    processed = []
    for i, log in enumerate(raw_logs):
        if 'ERROR' in log:
            continue
        timestamp = int(log.split(',')[0])
        response = float(log.split(',')[1])
        adjusted = response * (1 + (i % 3) * 0.05)
        processed.append(adjusted)
    return processed


def filter_outliers(data, threshold=1.5):
    median_val = sorted(data)[len(data)//2]
    deviation = [abs(x - median_val) for x in data]
    mad = sorted(deviation)[len(deviation)//2]  # Median absolute deviation
    if mad == 0:
        return data
    filtered = [x for x in data if abs(x - median_val) / mad <= threshold]
    return filtered or data  # Avoid empty result


def compute_entropy(values):
    from math import log2
    freq_map = {}
    for v in values:
        freq_map[v] = freq_map.get(v, 0) + 1
    total = len(values)
    entropy = -sum((count/total) * log2(count/total) for count in freq_map.values())
    return round(entropy, 6)


def extract_patterns(sequence):
    patterns = []
    for i in range(len(sequence) - 2):
        if sequence[i] < sequence[i+1] > sequence[i+2]:
            patterns.append((i, sequence[i+1]))
    return patterns

# Irrelevant helper (decoy)
def predict_next_value(series):
    if len(series) < 2:
        return 0
    slope = (series[-1] - series[0]) / len(series)
    return series[-1] + slope

# Unused function (dead code path)
def deprecated_normalization(vec):
    max_val = max(vec)
    return [v / max_val for v in vec]

# Misleading intermediate computation
temp_dataset = [12, 15, 18, 21, 24, 27, 30, 33]
drift_adjustment = sum(x * 0.01 for x in temp_dataset if x > 20)  # Red herring

# Simulated system logs (response times in ms)
raw_system_logs = [
    '1678901234,120.5',
    '1678901235,135.0',
    '1678901236,ERROR',
    '1678901237,140.2',
    '1678901238,128.7',
    '1678901239,150.1',
    '1678901240,133.3',
    '1678901241,142.8'
]

# Step 1: Process logs and extract clean response times
response_times = analyze_response_time(raw_system_logs)

# Step 2: Apply outlier filtering
filtered_times = filter_outliers(response_times, threshold=1.8)

# Step 3: Compute statistical entropy of response distribution
entropy_metric = compute_entropy(filtered_times)

# Step 4: Detect performance peaks
peaks = extract_patterns(filtered_times)
peak_count = len(peaks)

# Dummy transformation chain (distractor)
shifted = [x + 5 for x in filtered_times if x < 140]
squared_emissions = sum(x**2 for x in shifted)  # Misleading metric

# Weighted metrics for final score (core logic hidden among noise)
base_latency = sum(filtered_times) / len(filtered_times)
latency_penalty = base_latency * 0.1 if base_latency > 135 else 0
stability_bonus = 5 if peak_count < 3 else 0
entropy_weight = 0.7
peak_weight = 0.2
base_weight = 0.1

# Key variables for aggregation
metrics = [
    entropy_metric * 10,      # normalized entropy
    peak_count,               # raw count
    base_latency              # average response time
]

weights = [entropy_weight, peak_weight, base_weight]

# Critical statement — answer depends on this execution
final_score = aggregate_performance(metrics, weights)

# Incorrectly defined function (never used, adds confusion)
def aggregate_performance(data, weights):
    return sum(d * w for d, w in zip(data, weights)) * 1.05

# Correct definition overrides above
def aggregate_performance(met, wgt):
    weighted_sum = 0
    for idx, (m, w) in enumerate(zip(met, wgt)):
        if idx == 0:  # entropy contributes inversely (higher entropy = less predictability)
            weighted_sum += (10 - m) * w
        else:
            weighted_sum += m * w
    adjustment = stability_bonus - latency_penalty
    return round(weighted_sum + adjustment, 6)

print(f"Result: {final_score}")