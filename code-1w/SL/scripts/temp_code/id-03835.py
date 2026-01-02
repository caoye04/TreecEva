import math

def analyze_pattern(seq):
    # Irrelevant helper function (dead code path)
    return sum(1 for a, b in zip(seq, seq[1:]) if a < b)

def validate_entry(record):
    # Distractor: complex validation not used in main logic
    if not record.get('active'):
        return False
    checks = [
        record['value'] > 0,
        len(record['id']) == 5,
        record['flags'][0] != record['flags'][-1]
    ]
    return all(checks)

data = [
    {'id': 'X9P2Q', 'value': 120, 'active': True, 'metrics': [4, 8, 15], 'flags': [1, 0, 1]},
    {'id': 'Z7R1M', 'value': 89, 'active': False, 'metrics': [16, 23, 42], 'flags': [0, 1, 0]},
    {'id': 'L4T8N', 'value': 205, 'active': True, 'metrics': [1, 3, 2], 'flags': [1, 1, 1]},
    {'id': 'K9S5W', 'value': 73, 'active': True, 'metrics': [5, 5, 5], 'flags': [0, 0, 1]}
]

weights = {'w1': 0.3, 'w2': 0.5, 'w3': 0.2}  # Used in actual computation

# Irrelevant preprocessing (distractor)
preprocessed = []
for item in data:
    temp = {}
    temp['norm_value'] = item['value'] / max(d['value'] for d in data)
    temp['adjusted'] = [m * temp['norm_value'] for m in item['metrics']]
    preprocessed.append(temp)

# Unused transformation map (red herring)
transform_map = {
    'A': lambda x: x ** 2,
    'B': lambda x: int(math.sqrt(x)),
    'C': lambda x: x + 10
}

# Decoy aggregation using string methods (misleading)
flag_strings = [ ''.join(str(f) for f in item['flags']) for item in data ]
flag_stats = { s: s.count('1') * s.count('0') for s in flag_strings }

# Actual processing begins here
aggregated_metrics = []
for entry in data:
    raw = entry['metrics']
    # Only active entries contribute
    if not entry['active']:
        continue
    weighted_sum = raw[0] * weights['w1'] + raw[1] * weights['w2'] + raw[2] * weights['w3']
    adjusted_val = math.log(weighted_sum + 1) * entry['value']
    aggregated_metrics.append(adjusted_val)

# Secondary transformation with dictionary operations
metric_dict = { i: val for i, val in enumerate(aggregated_metrics) }

# Apply threshold filter (logical operation)
enabled_indices = [idx for idx, val in metric_dict.items() if val > 50 and idx in flag_stats.values()]

# Final processing function
def process_metrics(dataset, weight_config):
    total = 0.0
    count = 0
    for record in dataset:
        if not record['active']:
            continue  # Skip inactive
        m = record['metrics']
        w = weight_config
        score = m[0]*w['w1'] + m[1]*w['w2'] + m[2]*w['w3']
        if score > 10:  # Early threshold
            # Complex adjustment using string method on id
            bonus = len(record['id'].replace('X', '').strip()) * 0.1
            score += bonus
        total += score
        count += 1
    
    # Final nonlinear transformation
    final = math.floor(total * 1.25) if count > 1 else math.ceil(total)
    return int(final)

# Key execution point
final_score = process_metrics(data, weights)

# Print result as required
print(f"Result: {final_score}")