def analyze_trends(raw_values):
    # Irrelevant trend analysis (dead code path)
    moving_avg = [sum(raw_values[i:i+3]) / 3 for i in range(len(raw_values) - 2)]
    volatility = sum(abs(a - b) for a, b in zip(moving_avg, moving_avg[1:]))
    return volatility  # Not used in main logic


def preprocess_signals(input_stream):
    # Distractor: signal filtering with unused result
    filtered = [x for x in input_stream if x > 0.5]
    normalized = [x / max(filtered) for x in filtered]
    scaled = [int(x * 100) for x in normalized]
    return scaled[:10]  # Unused return


def compute_weight_vector(shape):
    # Red herring function: computes weights but not used in final path
    base = [i ** 0.5 for i in range(1, shape + 1)]
    weight_sum = sum(base)
    return [w / weight_sum for w in base]


def transform_dataset(data, key=3):
    # Bit manipulation decoy
    shifted = [(d << 2) ^ key for d in data]
    masked = [s & 0xFF for s in shifted]
    return [m if m % 2 == 0 else m + 1 for m in masked]


def evaluate_metric(entries):
    # Relevant transformation: extracts and filters valid entries
    valid_entries = [e for e in entries if isinstance(e, dict) and 'value' in e]
    values = [d['value'] for d in valid_entries]
    
    # Distractor: complex but irrelevant statistical moment calculation
    mean_val = sum(values) / len(values)
    variance = sum((v - mean_val) ** 2 for v in values) / len(values)
    skewness = sum((v - mean_val) ** 3 for v in values) / (len(values) * variance ** 1.5) if variance > 0 else 0
    
    # Core logic disguised among noise: count of high-value entries
    threshold = mean_val + (variance ** 0.5)
    high_count = sum(1 for v in values if v > threshold)
    
    # Decoy dictionary operations
    stats = {
        'mean': mean_val,
        'variance': variance,
        'skew': skewness,
        'high_count': high_count
    }
    metadata = {'processed': True, 'version': '2.1', 'debug': False}
    stats.update(metadata)
    
    return stats  # Only 'high_count' matters later


def evaluate_performance(metrics):
    # Main evaluation logic
    adjusted = metrics['high_count'] * 17
    penalty = 0
    
    # Simulated conditional penalties (mostly false)
    if metrics.get('skew', 0) > 1.0:
        penalty += 5
    elif metrics.get('outlier_ratio', 0) > 0.3:
        penalty += 10
    
    # Additional distraction: recursive bit counting (not affecting result)
    def count_bits(n):
        return 0 if n == 0 else (n & 1) + count_bits(n >> 1)
    
    temp_data = [12, 45, 67]
    bit_sum = sum(count_bits(x) for x in temp_data)  # Dead computation
    
    # Final score depends only on adjusted and constant offset
    final_score = adjusted - penalty + 4
    return final_score

# Irrelevant global variables
system_mode = "diagnostic"
config_flags = {"tracing": True, "verbose": False, "audit": None}
baseline_samples = list(range(5, 55, 5))

# Input data with mixed types and distractors
dataset = [
    {'value': 10}, {'value': 25}, {'name': 'missing'},
    {'value': 5}, {'value': 30}, {'value': 40, 'flag': True},
    'invalid', {'value': 15}, {'value': 50}
]

# Trigger preprocessing (results unused)
trends = analyze_trends([3, 7, 2, 8, 5])
signals = preprocess_signals([0.6, 0.9, 0.4, 0.7])
weights = compute_weight_vector(7)
transformed = transform_dataset([10, 20, 30])

# Core execution path
metric_data = evaluate_metric(dataset)
final_score = evaluate_performance(metric_data)

print(f"Result: {final_score}")