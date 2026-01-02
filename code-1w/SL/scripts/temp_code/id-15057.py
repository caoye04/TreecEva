def analyze_text(text):
    words = text.lower().split()
    word_lengths = [len(word) for word in words]
    avg_length = sum(word_lengths) / len(word_lengths) if words else 0
    unique_letters = len(set(''.join(words)))
    return avg_length, unique_letters

# Irrelevant helper function (decoy)
def calculate_entropy(data):
    from math import log2
    freq = {}
    total = len(data)
    for item in data:
        freq[item] = freq.get(item, 0) + 1
    entropy = -sum((count/total) * log2(count/total) for count in freq.values())
    return entropy

# Unused transformation chain
def transform_sequence(seq):
    if not seq:
        return []
    doubled = [x * 2 for x in seq]
    filtered = [x for x in doubled if x > 5]
    shifted = [x - 3 for x in filtered]
    return shifted

# Misleading metric computation (dead path)
def compute_legacy_metric(items):
    temp_result = 0
    for i in items:
        if i % 2 == 0:
            temp_result += i ** 2
        else:
            temp_result -= i
    adjustment = sum([i for i in items if i > 10])
    return temp_result + adjustment // 2

# Core logic disguised among noise
def preprocess_metrics(raw):
    cleaned = []
    for val in raw:
        if isinstance(val, str):
            try:
                cleaned.append(float(val.strip('$%')))
            except:
                continue
        elif isinstance(val, (int, float)) and val >= 0:
            cleaned.append(float(val))
    return [x for x in cleaned if x <= 1000]  # Filter outliers

def aggregate_indicators(values):
    if not values:
        return 0.0
    base = sum(values) / len(values)
    bonus = 0.0
    if len(values) > 5:
        bonus += 10.0
    if any(v > 90 for v in values):
        bonus += 5.0
    if all(v >= 30 for v in values):
        bonus += 7.5
    return base + bonus

def evaluate_performance(data):
    primary = aggregate_indicators(data['metrics'])
    context_factor = len(data['labels']) if data['labels'] else 1
    scaling = data.get('scale', 1.0)
    intermediate = primary * context_factor
    # Critical red herring: irrelevant bit manipulation
    mask = 0b101010
    masked = int(intermediate) & mask
    decoy_shift = masked << 2
    # Actual contribution: minor adjustment based on metadata
    meta_adjust = 0
    for k, v in data['meta'].items():
        if 'flag' in k and v:
            meta_adjust += 2.5
    final = intermediate * scaling + meta_adjust
    return final

# Irrelevant data structure
lookup_table = {
    'A': [1, 2], 'B': [3, 4], 'C': [5, 6],
    'X': [7, 8], 'Y': [9, 10]
}

# Unused recursive function (distractor)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Simulated input with mixed types and noise
dummy_payload = [
    "123", "$45.67", "abc", "99%", "0.5",
    -5, 1050, 88, "xyz", 72
]

# Real input data obscured among decoys
metric_data = {
    'metrics': preprocess_metrics([
        85, "92", "$78", "96%", 88, "0.7", 91, "invalid", 87
    ]),
    'labels': ['Q1', 'Q2', 'Q3', 'Q4'],
    'scale': 1.1,
    'meta': {
        'flag_alpha': True,
        'flag_beta': False,
        'flag_gamma': True,
        'extra': 'ignored'
    }
}

# Dead code path invocation (no effect)
test_seq = [1, 2, 3, 4]
transformed = transform_sequence(test_seq)
legacy_score = compute_legacy_metric([10, 20, 5, 15])

# Key execution point
final_score = evaluate_performance(metric_data)

# Noise output
entropy = calculate_entropy('aabbcc')
word_stats = analyze_text('The quick brown fox jumps over the lazy dog')

print(f"Result: {final_score}")