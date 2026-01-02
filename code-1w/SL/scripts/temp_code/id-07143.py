def analyze_data(records):
    # Irrelevant data transformation (distractor)
    processed = [r['value'] * 2 for r in records if r['active']]
    normalized = [p / max(processed) for p in processed]
    return normalized

# Decoy function that looks important but is unused
def compute_rankings(entries):
    rankings = {}
    for i, e in enumerate(sorted(entries, key=lambda x: x['score'], reverse=True)):
        rankings[e['id']] = i + 1
    return rankings

# Another decoy: complex but unused bitwise logic
def encrypt_key(base_key):
    key = base_key ^ 0xABCD
    key = (key << 3) & 0xFFFF
    key ^= (key >> 4)
    return key

# Set operations used meaningfully but with distractions
valid_ids = {101, 102, 103, 104, 105}
disqualified = {103, 107}
eligible_ids = valid_ids - disqualified

# Simulated input data
metrics = [
    {'type': 'accuracy', 'raw': 88.5},
    {'type': 'latency', 'raw': 42},
    {'type': 'throughput', 'raw': 156},
    {'type': 'energy', 'raw': 73}
]

weights = {
    'accuracy': 0.4,
    'latency': 0.1,
    'throughput': 0.3,
    'energy': 0.2
}

# Distractor variables
baseline_metrics = [m['raw'] for m in metrics]
adjusted_metrics = {m['type']: m['raw'] + 5 for m in metrics}  # Misleading adjustment

# Unused enumeration path
for idx, metric in enumerate(metrics):
    if metric['type'] == 'dummy':
        adjusted_metrics[metric['type']] *= 1.1  # Dead code branch

# Real logic buried among noise
transformed = []
for m in metrics:
    val = m['raw']
    if m['type'] == 'accuracy':
        val = val / 100.0
    elif m['type'] == 'latency':
        val = (100 - val) / 100.0  # Inverted
    else:
        val = min(val / 200.0, 1.0)
    transformed.append(val)

# Use of zip and enumerate together (required features)
eval_pairs = list(zip(transformed, weights.values()))
weighted_sum = 0
for i, (t_val, w) in enumerate(eval_pairs):
    contribution = t_val * w
    if i % 2 == 0:
        contribution *= 1.05  # Slight bias on even indices
    weighted_sum += contribution

# Secondary adjustment based on set membership (real use of set)
bonus_factor = 1.1 if len(eligible_ids) in {4, 5} else 1.0

# Critical statement
final_score = int(weighted_sum * bonus_factor * 1000)  # Scale to integer

# Output result as required
print(f"Result: {final_score}")