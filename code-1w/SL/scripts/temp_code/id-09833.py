import itertools

def analyze_pattern(sequence, threshold):
    count = 0
    for i in range(len(sequence) - 1):
        if sequence[i] < sequence[i+1]:
            count += 1
    return count > threshold

def normalize_data(data_list):
    max_val = max(data_list)
    return [x / max_val for x in data_list]

def compute_entropy(values):
    entropy = 0.0
    total = sum(values)
    for v in values:
        prob = v / total
        if prob > 0:
            entropy -= prob * __import__('math').log2(prob)
    return entropy

def filter_outliers(data, limit=3):
    mean = sum(data) / len(data)
    std = (__import__('math').sqrt(sum((x - mean)**2 for x in data) / len(data)))
    return [x for x in data if abs(x - mean) <= limit * std]

def generate_signature(keys):
    # Irrelevant function - red herring
    sig = 0
    for k in keys:
        sig ^= hash(str(k))
    return sig % 1000

def evaluate_performance(log, config):
    # Extract relevant metrics
    raw_metrics = log.get('metrics', [])
    processed = []
    
    temp_buffer = []
    for entry in raw_metrics:
        if 'value' in entry and entry.get('active', True):
            temp_buffer.append(entry['value'])
    
    # Normalize and filter
    normalized = normalize_data(temp_buffer)
    filtered = filter_outliers([x * 100 for x in normalized])
    
    # Compute derived statistics (some are distractions)
    avg = sum(filtered) / len(filtered)
    peak = max(filtered)
    volatility = sum(abs(filtered[i+1] - filtered[i]) for i in range(len(filtered)-1))
    
    # Bit manipulation decoy
    magic_flag = 0b1010
    shift_key = (len(filtered) % 8) or 1
    magic_flag = (magic_flag << shift_key) ^ 0b1100
    
    # Dummy dictionary operations with unused results
    summary_stats = {
        'count': len(filtered),
        'average': avg,
        'peak': peak,
        'volatility_index': volatility,
        'baseline_ref': config.get('ref', 50)
    }
    
    extra_analysis = {}
    for k in ['a', 'b', 'c']:
        extra_analysis[k] = (summary_stats['count'] * ord(k)) % 17
    
    # Real logic path: combinatorics on slices
    window_size = 3
    sliding_windows = [filtered[i:i+window_size] for i in range(0, len(filtered)-window_size+1, window_size)]
    
    valid_sequences = 0
    for window in sliding_windows:
        if len(window) == window_size:
            if analyze_pattern(window, 1):
                valid_sequences += 1
    
    # Use itertools to create distraction
    permutations_count = 0
    for _ in itertools.permutations([1, 2, 3]):
        permutations_count += 1  # Always 6, irrelevant
    
    # Core calculation involving multiple concepts
    entropy_metric = compute_entropy([valid_sequences + 1, len(sliding_windows) + 1])
    adjustment_factor = summary_stats['baseline_ref'] / 100.0
    
    # Final score depends only on specific chain: valid_sequences * adjustment scaling
    base_score = valid_sequences * 100
    penalty = len(sliding_windows) - valid_sequences  # missed patterns
    final_score = base_score - (penalty * 10)  # Each missed window costs 10 points
    
    # Dead code path - never executed due to logic
    if magic_flag < 0:
        fallback = generate_signature(extra_analysis.keys())
        final_score = fallback
    
    return int(final_score)

# Simulated input data
baseline_config = {
    'ref': 75,
    'mode': 'strict',
    'thresholds': [0.5, 0.7, 0.9]
}

metrics_log = {
    'timestamp': 1712345678,
    'version': '2.3.1',
    'metrics': [
        {'value': 10, 'active': True},
        {'value': 15, 'active': True},
        {'value': 12, 'active': True},
        {'value': 18, 'active': True},
        {'value': 16, 'active': True},
        {'value': 20, 'active': True},
        {'value': 19, 'active': True},
        {'value': 25, 'active': True},
        {'value': 22, 'active': True}
    ],
    'debug': True,
    'tags': ['stable', 'final']
}

# Execution point of interest
final_score = evaluate_performance(metrics_log, baseline_config)
print(f"Result: {final_score}")