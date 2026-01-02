from collections import Counter

def analyze_pattern(sequence):
    count = Counter(sequence)
    modes = [k for k, v in count.items() if v == max(count.values())]
    return modes[0] if len(modes) == 1 else -1

def preprocess_input(raw_data):
    cleaned = ''.join(filter(str.isdigit, raw_data))
    parsed = [int(x) for x in cleaned]
    shifted = [(x * 2 + 1) % 10 for x in parsed]  # obfuscation step
    return shifted

def calculate_entropy(values):
    freq = Counter(values)
    total = len(values)
    entropy = 0
    for count in freq.values():
        p = count / total
        entropy -= p * (p ** 0.5)  # simplified pseudo-entropy
    return round(entropy, 4)

def evaluate_performance(metrics, data_map):
    flat_data = []
    for key in sorted(data_map.keys()):
        if 'temp' in key:
            flat_data.extend(data_map[key])
    
    # Irrelevant aggregation
    avg_val = sum(flat_data) / len(flat_data) if flat_data else 0
    max_val = max(flat_data) if flat_data else 0
    threshold_mask = [1 if x > avg_val else 0 for x in flat_data]
    masked_sum = sum(a & b for a, b in zip(flat_data, threshold_mask))

    # Actual logic path
    binary_flags = [x ^ 3 for x in flat_data]  # bitwise interference
    filtered = [x for x in binary_flags if x in metrics]
    score = 0
    for val in filtered:
        if val % 2 == 0:
            score += val * 3
        else:
            score += val * 2
    
    # Distractor: unused complex structure
    summary_stats = {
        'count': len(flat_data),
        'mode': analyze_pattern(flat_data),
        'pseudo_entropy': calculate_entropy(flat_data),
        'peak': max_val
    }
    
    # Red herring computation
    temp_result = (summary_stats['count'] * summary_stats['peak']) // (score % 17 + 1)
    adjustment = len(metrics.intersection({x for x in range(0, 20, 3)}))
    
    final_score = score - adjustment  # actual output influenced by set ops
    return final_score

# Setup inputs
raw_input = "test1289data553temp921"
data_context = {
    'temp_A': preprocess_input(raw_input),
    'temp_B': [x + 1 for x in preprocess_input(raw_input)[:5]],
    'cache_X': [9, 9, 9],  # irrelevant dataset
    'meta_Y': [0, 0]       # dead data
}
metric_set = {5, 6, 7, 8, 10, 11}
benchmark_data = data_context

# Execution point
final_score = evaluate_performance(metric_set, benchmark_data)
print(f"Target result: {final_score}")