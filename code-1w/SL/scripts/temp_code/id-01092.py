from collections import defaultdict, Counter
import math

# Simulated system telemetry data (distractor)
telemetry_log = [
    {'timestamp': 1001, 'event': 'input_scan', 'value': 3.14},
    {'timestamp': 1002, 'event': 'buffer_flush', 'value': 2.71},
    {'timestamp': 1003, 'event': 'input_scan', 'value': 1.41}
]

total_telemetry_value = sum(entry['value'] for entry in telemetry_log if entry['event'] == 'input_scan')
telemetry_count = len(telemetry_log)

# Core data structures for evaluation (relevant)
metric_data = [
    {'name': 'latency', 'raw': 450, 'units': 'ms'},
    {'name': 'throughput', 'raw': 876, 'units': 'req/s'},
    {'name': 'error_rate', 'raw': 23, 'units': '%'},
    {'name': 'concurrency', 'raw': 120, 'units': 'threads'}
]

user_weights = {
    'latency': 0.4,
    'throughput': 0.35,
    'error_rate': -0.2,  # Negative impact
    'concurrency': 0.1
}

# Irrelevant transformation chain (red herring)
def transform_chain(x):
    a = x ** 2 + 3 * x + 1
    b = int(math.sqrt(a)) if a > 0 else 0
    c = (b >> 2) ^ 0x1F
    return c  # Never meaningfully used

intermediate_seq = [transform_chain(i) for i in range(5)]
shadow_buffer = [x * 1.05 for x in intermediate_seq]

# Decoy scoring function (dead path)
def compute_legacy_score(data_map):
    score = 0
    for k, v in data_map.items():
        if 'rate' in k:
            score -= v * 1.5
        else:
            score += v // 10
    return score * 0.8

# Auxiliary analysis (partially relevant but misleading)
analysis_grid = defaultdict(list)
for entry in metric_data:
    category = 'performance' if entry['name'] in ['latency', 'throughput'] else 'stability'
    analysis_grid[category].append(entry['raw'])

size_factor = len(analysis_grid['performance']) * len(analysis_grid.get('stability', [1]))
baseline_projection = sum(analysis_grid['performance']) / size_factor

# Character frequency distraction
text_corpus = "throughput latency concurrency error_rate"
counts = Counter(text_corpus.replace("_", ""))
most_frequent_char = counts.most_common(1)[0][1]  # 'e' appears most

# Real processing begins here
NORMALIZATION_REF = 1000
def normalize_metric(value, metric_name):
    if metric_name == 'latency':
        return (NORMALIZATION_REF - value) / NORMALIZATION_REF
    elif metric_name == 'error_rate':
        return 1 - (value / 100)
    else:
        return min(value / NORMALIZATION_REF, 1.0)

# Main evaluation logic
weighted_components = []
for item in metric_data:
    norm_val = normalize_metric(item['raw'], item['name'])
    weight = user_weights[item['name']]
    weighted_components.append(norm_val * abs(weight))

composite_base = sum(weighted_components) * 500  # Scale to integer-friendly range

def adjust_for_balance(score, components):
    # Simulate balance penalty based on variance
    mean_val = sum(components) / len(components)
    variance = sum((x - mean_val) ** 2 for x in components) / len(components)
    adjustment = math.exp(-variance * 10)  # Strong sensitivity
    return score * adjustment

# Apply balance correction
balanced_score = adjust_for_balance(composite_base, weighted_components)

# Final aggregation with irrelevant context merge
context_enhancement = 1 + (most_frequent_char / 1000)  # Minor red herring
raw_final = balanced_score * context_enhancement

# Key assignment - this is where the answer is determined
final_score = int(round(raw_final + baseline_projection - total_telemetry_value))

# Output result as required
print(f"Result: {final_score}")