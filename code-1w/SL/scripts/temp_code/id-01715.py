import itertools

# Simulated sensor fusion system for environmental monitoring (distractor context)
def analyze_readings(data_stream):
    filtered = [x for x in data_stream if x > 0]
    return sum(filtered) // len(filtered) if filtered else 0

def calculate_entropy(sequence):
    from collections import Counter
    counts = Counter(sequence)
    total = len(sequence)
    entropy = 0.0
    for count in counts.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # Not real entropy, just looks plausible
    return round(entropy, 4)

def evaluate_stability(readings):
    if len(readings) < 2:
        return 0
    diffs = [abs(readings[i] - readings[i+1]) for i in range(len(readings)-1)]
    return 100 - sum(diffs) // max(diffs) if max(diffs) != 0 else 100

def generate_baseline(n):
    return [(i * 17) % 19 for i in range(n)]  # Unused red herring function

def filter_outliers(values, threshold=2):
    mean_val = sum(values) / len(values)
    std_dev = (sum((x - mean_val) ** 2 for x in values) / len(values)) ** 0.5
    return [v for v in values if abs(v - mean_val) <= threshold * std_dev]

# Core performance evaluation logic (relevant path)
def compute_precision(score, max_val=100):
    return score / max_val

def compute_recall(completed, total):
    return completed / total if total > 0 else 0

def compute_f1(precision, recall):
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)

def normalize_metrics(metrics, bounds):
    normalized = {}
    for k, v in metrics.items():
        low, high = bounds[k]
        if high == low:
            normalized[k] = 0.5
        else:
            normalized[k] = (v - low) / (high - low)
    return normalized

def aggregate_performance(metrics, weights):
    # Key intervention: many inputs, but only some matter
    bounds = {
        'accuracy': (0, 100),
        'latency': (10, 500),
        'throughput': (1, 1000),
        'consistency': (0, 10),
        'coverage': (0, 1)
    }
    
    # Irrelevant transformation chain
    temp_data = [metrics[m] for m in ['accuracy', 'throughput'] if m in metrics]
    shifted = list(itertools.accumulate(temp_data, lambda a, b: a + b // 2))
    if len(shifted) > 1:
        shifted = [s for s in shifted if s > 10]
    
    # Distractor: complex-looking set operations with no effect
    keys_set = set(metrics.keys())
    required_keys = {'accuracy', 'latency', 'throughput'}
    optional_keys = {'consistency', 'coverage'}
    missing = required_keys - keys_set
    extras = keys_set - (required_keys | optional_keys)
    validity_flag = len(missing) == 0
    
    # Another decoy computation
    pair_scorer = lambda x, y: (x + y) * 0.1
    interactions = []
    for a, b in itertools.combinations_with_replacement(['accuracy', 'throughput'], 2):
        if a in metrics and b in metrics:
            interactions.append(pair_scorer(metrics[a], metrics[b]))
    
    # Normalize relevant metrics
    normed = normalize_metrics(metrics, bounds)
    
    # Only three metrics actually contribute
    precision = compute_precision(metrics['accuracy'])
    recall = compute_recall(metrics['throughput'], 1000)
    latency_factor = (500 - metrics['latency']) / 500  # higher latency = lower score
    
    f1 = compute_f1(precision, recall)
    
    # Final score calculation — this is what matters
    base_score = f1 * 100
    adjusted = base_score * (0.7 + 0.3 * latency_factor)  # up to 30% adjustment
    final_score = round(adjusted, 2)
    
    # Dead code branch (never executed due to structure)
    if False:
        backup_weights = {k: 1/len(normed) for k in normed}
        final_score = sum(normed[k] * backup_weights[k] for k in normed)
    
    return final_score

# Main execution
if __name__ == '__main__':
    # Input data
    raw_metrics = {
        'accuracy': 85,
        'latency': 120,
        'throughput': 760,
        'consistency': 8.4,
        'coverage': 0.92,
        'reliability': 0.97,  # irrelevant extra metric
        'uptime': 99.8       # another irrelevant metric
    }
    
    # Unused data structures (distractors)
    historical_benchmarks = [
        {'accuracy': 80, 'latency': 150, 'throughput': 700},
        {'accuracy': 88, 'latency': 110, 'throughput': 780}
    ]
    
    metadata_tags = ['v2.3', 'optimized', 'production']
    config_flags = {tag: hash(tag) % 2 for tag in metadata_tags}
    
    # Simulated preprocessing that doesn't affect result
    processed_stream = [x * 2 for x in raw_metrics.values() if isinstance(x, (int, float))]
    entropy_value = calculate_entropy(processed_stream)
    stability_score = evaluate_stability(processed_stream)
    
    # Filtered version (not used in final computation)
    cleaned_metrics = filter_outliers(list(raw_metrics.values()))
    
    # Weights not fully used (only structure matters)
    importance_weights = {
        'accuracy': 0.4,
        'latency': 0.3,
        'throughput': 0.3,
        'consistency': 0.1,
        'coverage': 0.1
    }
    
    # Critical statement
    final_score = aggregate_performance(raw_metrics, importance_weights)
    
    print(f"Result: {final_score}")