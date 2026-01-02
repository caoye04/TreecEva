from collections import defaultdict, Counter

# Irrelevant helper function (dead code path)
def analyze_sentiment(text):
    return sum(1 for c in text if c in 'aeiou') % 3

def compute_hash(s):
    # Distractor: looks important but unused in final logic
    return sum(ord(c) * (i + 1) for i, c in enumerate(s)) % 1000

# Misleading data initialization
temp_records = [
    {'id': 'A', 'val': 120, 'flag': True},
    {'id': 'B', 'val': 85, 'flag': False},
    {'id': 'C', 'val': 95, 'flag': True}
]

# Decoy transformation pipeline
transform = lambda x: x ** 2 - x * 3 + 2
processed = [transform(record['val']) for record in temp_records if record['flag']]

# Real data starts here
raw_input = "45,67,89,23,78,56,34,90,12,67"
data = list(map(int, raw_input.split(',')))

# Weight mapping with extra keys (red herring)
weights = {
    'A': 0.1,
    'B': 0.2,
    'C': 0.35,
    'D': 0.15,
    'X': 0.05,  # Unused weight
    'Y': 0.07   # Another decoy
}

# Auxiliary counting using Counter (legitimate use)
element_counts = Counter(data)
common_pairs = [k for k, v in element_counts.items() if v > 1]

# Bit manipulation distraction
bit_flags = 0
for val in data:
    bit_flags ^= (val & 7) << 2
    bit_flags += val % 5

# String-based decoy processing
dummy_text = "metric_eval_2024"
shift_key = sum(ord(c) for c in dummy_text if c.isdigit())

# Real computation begins
scaling_factor = 1.75
adjusted = [x * scaling_factor for x in data if x > 25]

# Filtering and grouping with defaultdict (relevant)
grouped = defaultdict(list)
for val in adjusted:
    key = int(val // 50)
    grouped[key].append(val)

central_tendency = {}
for k, vals in grouped.items():
    sorted_vals = sorted(vals)
    mid = len(sorted_vals) // 2
    # Use median as representative
    central_tendency[k] = (sorted_vals[mid] + sorted_vals[~mid]) / 2

# Secondary filter: only groups with more than 2 elements
effective_values = [v for v in central_tendency.values() if len(grouped[int(v // 50)]) >= 3]

# Apply weighted combination using only A, B, C, D weights
weight_sum = sum(weights[w] for w in 'ABCD')
normalized_weights = {w: weights[w] / weight_sum for w in 'ABCD'}

# Simulate multi-metric fusion
metrics = {
    'A': sum(effective_values) / len(effective_values) if effective_values else 0,
    'B': max(effective_values) * 0.9 if effective_values else 0,
    'C': min(effective_values) * 1.1 if effective_values else 0,
    'D': (sum(v**2 for v in effective_values) / len(effective_values))**0.5 if effective_values else 0
}

# Final score calculation
process_metrics = lambda d, w: sum(metrics[key] * w[key] for key in 'ABCD')

final_score = process_metrics(data, weights)

# Output result
print(f"Result: {final_score}")