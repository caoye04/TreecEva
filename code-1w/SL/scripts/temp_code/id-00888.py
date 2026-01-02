from itertools import combinations, cycle
import math

# Irrelevant data structures and constants (distractors)
legacy_codes = [0xABC, 0xDEF, 0xCAFE, 0xBABE]
dummy_mapping = {'A': 1, 'B': 2, 'C': 3}
phantom_counter = sum([len(str(x)) for x in legacy_codes])

# Real input data
sensor_readings = [14.5, 17.2, 15.8, 20.1, 18.3, 16.7, 19.0]

def generate_patterns(seq, depth=2):
    # Distractor function: generates unused combinatorial patterns
    return list(combinations(seq, depth))

def calculate_entropy(values):
    # Unused but plausible-sounding metric
    norm = [v / sum(values) for v in values]
    return -sum(p * math.log(p) for p in norm if p > 0)

# Simulated historical baseline (mostly irrelevant)
historical_trends = list(zip(sensor_readings[:-1], sensor_readings[1:]))
trend_ratios = [b/a for a, b in historical_trends if a != 0]
baseline_drift = sum(trend_ratios) / len(trend_ratios) if trend_ratios else 0

# Core processing functions

def filter_outliers(data, threshold=1.5):
    mean = sum(data) / len(data)
    std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
    return [x for x in data if abs(x - mean) <= threshold * std_dev]

def rolling_average(series, window=3):
    if len(series) < window:
        return [sum(series)/len(series)]
    avgs = [(sum(series[i:i+window])/window) for i in range(len(series)-window+1)]
    return avgs

def compute_skewness(data):
    n = len(data)
    mean = sum(data) / n
    variance = sum((x - mean)**2 for x in data) / n
    std_dev = variance ** 0.5
    if std_dev == 0:
        return 0
    skew = sum(((x - mean)/std_dev)**3 for x in data) * (n / ((n-1)*(n-2)))
    return skew

# Secondary metrics with partial relevance
filtered_readings = filter_outliers(sensor_readings, 1.8)
smoothed_signal = rolling_average(filtered_readings, 2)
noise_estimate = sum(abs(smoothed_signal[i] - smoothed_signal[i-1]) 
                      for i in range(1, len(smoothed_signal)))

# Decoy branching logic (never executed)
if __debug__:
    debug_snapshot = sensor_readings[:]
else:
    debug_snapshot = None

# Conditional expression (required python feature)
activation_mode = 'high_precision' if len(filtered_readings) > 5 else 'fallback'

# Generate multiple unused diagnostics (red herrings)
diagnostic_pool = []
for i, val in enumerate(cycle([2, 3])):
    if i >= 10:
        break
    diagnostic_pool.append((i * val) % 7)

# Actual relevant computation chain
primary_metric = compute_skewness(filtered_readings)
secondary_metric = len(smoothed_signal) * 1.5

# Aggregation with distraction from dummy variables
aggregate_diagnostics = [
    primary_metric * 100,
    secondary_metric,
    noise_estimate,
    sum(diagnostic_pool[:4]),  # Partial use of decoy list
    phantom_counter  # Irrelevant insertion
]

baseline_threshold = 42.0  # Fixed reference point

# Key statement
final_diagnostic = process_metrics(aggregate_diagnostics, baseline_threshold)

# Implementation of required function (hidden in middle)
def process_metrics(metrics, threshold):
    # Real decision logic buried in complexity
    adjusted = [m for m in metrics if isinstance(m, (int, float)) and m >= 0]
    if not adjusted:
        return 0
    # Focus on first three real metrics, ignore injected noise
    core = adjusted[:3]
    score = sum(core) - threshold  # Net effect
    # Conditional expression again
    return round(score, 4) if score > 0 else int(score // 1)

# Print result as required
Result: {final_diagnostic}