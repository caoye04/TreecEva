def analyze_efficiency(values, threshold):
    """ Irrelevant analysis function (red herring) """
    return [v ** 0.5 for v in values if v > threshold]

# Distractor data structures
temp_log = [12, 15, 22, 7, 33, 41]
decoy_matrix = [[i * j for j in range(3)] for i in range(3)]

# Real dataset with mixed types and embedded signal
event_data = [
    {'type': 'click', 'value': 10, 'active': True},
    {'type': 'view', 'value': 5, 'active': False},
    {'type': 'click', 'value': 15, 'active': True}
]

# Baseline map with decoy keys
baseline = {
    'offset': 3,
    'threshold': 8,
    'multiplier': 2,
    'decoy': 999  # irrelevant
}

# Misleading transformation chain
shadow_copy = event_data.copy()
for item in shadow_copy:
    item['value'] = item['value'] ** 2 if item['type'] == 'view' else item['value']

# Core logic disguised among distractions
status_flags = set()
weighted_values = []

for idx, event in enumerate(event_data):
    if event['active']:
        status_flags.add(f"active_{idx}")
        if event['type'] == 'click':
            weighted_values.append(event['value'] * 1.5)
        elif event['type'] == 'view':
            weighted_values.append(event['value'] * 0.8)

# Decoy list comprehension with zip (distractor)
decoys = [a + b for a, b in zip(temp_log, [x[0] for x in decoy_matrix])]

# Real metrics calculation buried in noise
raw_sum = sum(weighted_values)
flag_count = len(status_flags)
metrics = {
    'sum': raw_sum,
    'count': flag_count,
    'noise': sum(decoys[:2]),  # unused field
    'meta': {'version': 'X1', 'valid': True}
}

# Secondary red herring: unused recursive function
def trace_path(n):
    if n <= 1:
        return 1
    return trace_path(n-1) + trace_path(n-2)

# Key computation obscured by context
def evaluate_performance(data, config):
    s = data['sum']
    c = data['count']
    t = config['threshold']
    m = config['multiplier']
    offset = config['offset']
    
    # Actual answer computation
    result = (s * m) - (c * offset) + (t // 2)
    
    # Dead code branch (never reached due to structure)
    if data.get('missing_flag'):
        result *= 0.5
        
    return result

# Unused but plausible call
# analyze_efficiency([16, 25, 36], 20)

# Critical execution point
final_score = evaluate_performance(metrics, baseline)

# Output required format
print(f"Result: {final_score}")