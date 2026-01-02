from collections import defaultdict, Counter
import itertools

# Simulated sensor network diagnostic system
node_readings = [
    [14, 17, 23, 15, 19],
    [22, 18, 24, 20, 21],
    [13, 16, 19, 14, 18],
    [25, 27, 23, 26, 24],
    [17, 15, 18, 20, 16]
]

# Irrelevant statistical smoothing (distractor)
def smooth_signal(signal):
    return [sum(signal[i:i+3]) / 3 for i in range(len(signal)-2)]

# Unused legacy function (dead code path)
def legacy_calibrate(x):
    return (x * 0.97) + 3

# Core processing pipeline
def compute_variance(values):
    mean = sum(values) / len(values)
    return sum((x - mean) ** 2 for x in values) / len(values)

def detect_anomalies(cluster):
    var = compute_variance(cluster)
    return var > 15

def generate_frequencies(data):
    freq = defaultdict(int)
    for val in itertools.chain.from_iterable(data):
        freq[val] += 1
    return freq

# Misleading intermediate analysis (red herring)
aggregated_values = list(itertools.chain.from_iterable(node_readings))
value_counts = Counter(aggregated_values)
peak_frequency = max(value_counts.values())

# Dummy normalization attempt (irrelevant)
normalized_peaks = [round((v - 10) / 2) for v in value_counts if value_counts[v] == peak_frequency]

# Real signal: identify high-variance nodes
critical_nodes = []
for i, node in enumerate(node_readings):
    if detect_anomalies(node):
        critical_nodes.append(i)

# Compute trend signature from non-critical nodes
valid_trends = []
for i, node in enumerate(node_readings):
    if i not in critical_nodes:
        valid_trends.append(sum(node) / len(node))

trend_data = [round(x * 1.07) for x in valid_trends]  # Apply gain factor

# Baseline derived from frequency mode
sorted_vals = sorted(aggregated_values)
baseline = sorted_vals[len(sorted_vals) // 2]  # Median as baseline

# Decoy buffer calculation (misleading)
temp_buffer = sum(1 for x in value_counts.values() if x > 1)
scratch_metric = sum(abs(baseline - x) for x in trend_data)

# Actual aggregation function
def aggregate_metrics(metrics, base):
    shift = len(metrics) if metrics else 1
    total = 0
    for idx, val in enumerate(metrics):
        total += (val - base) * (idx + 1)
    return total * shift

# Outlier detection with dummy fallback
if len(critical_nodes) > 2:
    outlier_buffer = len(critical_nodes)
else:
    outlier_buffer = 8  # Default safety buffer

# Key statement — target execution point
final_diagnostic = aggregate_metrics(trend_data, baseline) // outlier_buffer

# Print result for evaluation
print(f"Result: {final_diagnostic}")