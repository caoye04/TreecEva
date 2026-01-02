def analyze_trends(data, threshold=5):
    trend_scores = []
    for i, value in enumerate(data):
        if value > threshold:
            trend_scores.append(value * 0.8)
        else:
            trend_scores.append(value * 1.2)
    return trend_scores

# Irrelevant helper function (decoy)
def calculate_baseline(x):
    return sum(x) / len(x) if x else 0

# Another decoy function with misleading intermediate computation
def assess_risk_level(values):
    risk = 0
    for v in values:
        if v > 10:
            risk += v ** 0.5
    return int(risk % 7)

# Core data processing chain
def transform_signals(signals):
    processed = []
    for s in signals:
        if s < 0:
            processed.append(abs(s) ^ 3)  # Bitwise XOR distraction
        elif s == 0:
            processed.append(777)  # Red herring value
        else:
            processed.append(s + (s & 5))  # Bitwise AND used meaningfully
    return processed

def filter_outliers(seq, limit=100):
    return [x for x in seq if x <= limit]

# String-based distractor: uses string methods but irrelevant
def generate_report_key(tags):
    cleaned = [t.strip().lower() for t in tags]
    joined = ''.join(joined for joined in cleaned)  # Obfuscated join
    return hash(joined) % 1000

# Set operation distractor
def compute_unique_groups(a, b):
    set_a, set_b = set(a), set(b)
    return len(set_a.symmetric_difference(set_b))

# Main evaluation logic
def evaluate_performance(metrics, weights):
    weighted_sum = 0.0
    norm_factor = sum(weights)
    
    # Real logic embedded among distractions
    for idx, (m, w) in enumerate(zip(metrics, weights)):
        adj_metric = m * (0.9 + 0.2 * (idx % 2))
        weighted_sum += adj_metric * w
    
    # Decoy calculation with misleading name
    pseudo_entropy = 0
    for x in metrics:
        if x > 0:
            pseudo_entropy += x * math.log(x)
    
    # Actual result influenced by control flow and arithmetic
    if weighted_sum > 50:
        final = weighted_sum * 0.95
    else:
        final = weighted_sum * 1.1
    
    return int(final)

# Irrelevant data structures
auxiliary_data = [
    {'id': 'A', 'val': 12},
    {'id': 'B', 'val': 15}
]
temp_cache = {i: i**2 for i in range(10)}

# Distractor variables
baseline_offset = 3.14159
dummy_flag = True
placeholder_list = [1, 1, 2, 3, 5, 8]  # Fibonacci red herring

# Real input data
raw_metrics = [8, 12, 6, 14, 9]
weights = [0.2, 0.3, 0.1, 0.25, 0.15]

# Transformations with mixed relevance
transformed_metrics = transform_signals(raw_metrics)
cleaned_metrics = filter_outliers(transformed_metrics)

# More distractions
feature_tags = ['SignalA ', ' DataFlow ', ' ControlX ']
key_code = generate_report_key(feature_tags)
group_diff = compute_unique_groups([1,2,3], [3,4,5])

# Trend analysis (unused path)
trends = analyze_trends(raw_metrics)

# Critical execution point
final_score = evaluate_performance(cleaned_metrics, weights)

# Output result as required
print(f"Result: {final_score}")