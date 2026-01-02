import itertools

def analyze_trends(data, threshold=5):
    trends = []
    for i in range(1, len(data)):
        if data[i] - data[i-1] > threshold:
            trends.append('up')
        elif data[i-1] - data[i] > threshold:
            trends.append('down')
        else:
            trends.append('stable')
    return trends

def compute_entropy(values):
    from math import log2
    freq = {}
    for v in values:
        freq[v] = freq.get(v, 0) + 1
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * log2(p)
    return round(entropy, 6)

def filter_outliers(seq, factor=1.5):
    if len(seq) == 0:
        return seq
    sorted_seq = sorted(seq)
    q1, q3 = sorted_seq[len(sorted_seq)//4], sorted_seq[3*len(sorted_seq)//4]
    iqr = q3 - q1
    lower, upper = q1 - factor * iqr, q3 + factor * iqr
    return [x for x in seq if lower <= x <= upper]

def merge_configs(base, override):
    # Dead function - not used in main logic
    result = base.copy()
    for k, v in override.items():
        if isinstance(v, dict) and k in result:
            result[k] = merge_configs(result[k], v)
        else:
            result[k] = v
    return result

def evaluate_performance(metrics, ref):
    score = 0
    temp_log = []
    
    # Irrelevant config block (distractor)
    system_config = {
        'version': '2.3.1',
        'mode': 'production',
        'debug': False,
        'timeout': 30
    }
    
    # Real computation begins
    keys = ['latency', 'throughput', 'consistency', 'reliability']
    weights = {'latency': 0.3, 'throughput': 0.4, 'consistency': 0.2, 'reliability': 0.1}
    
    normalized = {}
    for k in keys:
        raw = metrics.get(k, 0)
        baseline = ref.get(k, 1)
        if baseline > 0:
            normalized[k] = min(raw / baseline, 2.0)

    # Compute weighted score
    for k in keys:
        if k in normalized:
            contribution = normalized[k] * weights[k] * 100
            score += contribution

    # Bit manipulation red herring
    magic_offset = 0
    for i in range(3):
        magic_offset ^= (score >> i) & 7
    magic_offset = (magic_offset << 2) ^ 17

    # Decoy transformation using itertools
    expanded = list(itertools.chain.from_iterable([(x, x*2) for x in [1, 2, 3]]))
    fake_adjustment = sum(expanded) % 97

    # Set operation distractor
    expected_tags = {'A', 'B', 'C', 'D'}
    actual_tags = {'B', 'C'}
    missing = expected_tags - actual_tags
    tag_penalty = len(missing) * 5

    # Real adjustment: only this affects final_score
    stability_check = metrics.get('consistency', 0) >= 0.85
    reliability_threshold = metrics.get('reliability', 0) > 0.9
    if stability_check and reliability_threshold:
        score += 15

    # Final irrelevant block
    audit_trail = []
    for _ in range(2):
        audit_trail.append(f"Processed at level {_ + 1}")

    final_score = int(score)
    print(f"Result: {final_score}")
    return final_score

# Main execution
metric_data = {
    'latency': 45,
    'throughput': 92,
    'consistency': 0.92,
    'reliability': 0.93,
    'jitter': 12,
    'uptime': 99.7
}
benchmark = {
    'latency': 60,
    'throughput': 80,
    'consistency': 0.85,
    'reliability': 0.9
}
data_stream = [4, 5, 6, 6, 7, 8, 9, 9, 9, 10]

# Unused variables (red herrings)
config_override = {'debug': True, 'timeout': 60}
baseline_entropy = compute_entropy(data_stream)
trend_analysis = analyze_trends(data_stream)
cleaned_metrics = filter_outliers([45, 92, 88, 76, 95, 102, 34])

# Key statement
final_score = evaluate_performance(metric_data, benchmark)