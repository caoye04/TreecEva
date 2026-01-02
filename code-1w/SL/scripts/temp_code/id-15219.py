def analyze_text(text):
    words = text.split()
    word_lengths = [len(word.strip('.,!?"')) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0
    uppercases = sum(1 for c in text if c.isupper())
    exclamation_count = text.count('!')
    return avg_length, uppercases, exclamation_count

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    from math import log2
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return entropy

# Unused sorting function (dead code path)
def sort_by_priority(items):
    return sorted(items, key=lambda x: (x[1], -len(x[0])))

# Misleading data transformation
def transform_metrics(raw):
    transformed = {}
    for k, v in raw.items():
        if 'count' in k:
            transformed[k] = v * 1.5
        elif 'score' in k:
            transformed[k] = v ** 0.9
        else:
            transformed[k] = v + 10
    return transformed

# Distractor variables
baseline_config = {
    'threshold': 7.2,
    'weight_a': 0.6,
    'weight_b': 0.4,
    'offset': -5,
    'scale_factor': 1.8
}

# Unused complex structure
decoys = [
    {'id': 'd001', 'payload': [1, 1, 2, 3, 5, 8], 'active': False},
    {'id': 'd002', 'payload': [2, 4, 8, 16], 'active': False}
]

# Relevant recursive function with distractors
def compute_adaptive_weight(n, depth=0):
    if n <= 1 or depth > 5:
        return 1
    if n % 2 == 0:
        return 0.7 * compute_adaptive_weight(n // 2, depth + 1)
    else:
        return 1.2 * compute_adaptive_weight(n - 1, depth + 1)

# Core logic hidden among noise
def evaluate_performance(metrics, base):
    # Key intermediate values
    raw_value = metrics['event_count'] * base['weight_a']
    adjustment = len(metrics['labels']) * 3
    
    # Real computation path
    temp = raw_value + adjustment
    
    # Red herring: irrelevant bit manipulation
    flag = 0b1010
    mask = 0b1100
    masked = flag & mask
    shifted = masked << 2
    
    # Another decoy calculation
    dummy_result = (metrics['event_count'] ^ 15) | 7
    
    # Actual relevant logic
    score_component = temp * compute_adaptive_weight(len(metrics['labels']))
    
    # Conditional that always triggers due to input constraints
    if metrics['event_count'] > 0:
        score_component += base['offset']

    # String-based dispatch (uses string method)
    mode = 'standard_enhanced'
    if mode.endswith('enhanced'):
        score_component *= 1.25
    
    return int(score_component)

# Setup data with meaningful and irrelevant parts
log_entry = "System event triggered: CRITICAL ERROR on Node-7! Immediate action required!"

# Extract some real features
avg_len, uppers, exclamations = analyze_text(log_entry)

# Build metric data (only some fields are used)
metric_data = {
    'event_count': 12,
    'labels': ['critical', 'system', 'urgent'],
    'timestamp_str': '2023-11-05T14:32:00Z',
    'exclamation_marks': exclamations,
    'average_word_length': avg_len,
    'uppercase_chars': uppers
}

# Dead code: unused transformation
processed_data = transform_metrics(metric_data)

# Final evaluation (key statement)
final_score = evaluate_performance(metric_data, baseline_config)

print(f"Result: {final_score}")