def process_results(entries, importance):
    base_map = {k: len(v) for k, v in entries.items()}
    
    # Irrelevant transformation
    temp_caps = {k.upper(): ''.join(sorted(v)) for k, v in entries.items()}
    dummy_sum = sum(len(val) for val in temp_caps.values())

    # Distractor list processing
    outliers = []
    for key, value in base_map.items():
        if value > 3:
            outliers.append(key)
    
    # Actual computation begins
    weighted_vals = map(lambda kv: base_map[kv[0]] * importance.get(kv[0], 1.0), entries.items())
    adjustment = 0.0
    for i, val in enumerate(weighted_vals):
        if i % 2 == 0:
            adjustment += val * 0.1
    
    # Secondary irrelevant structure
    stats = {}
    for k, v in entries.items():
        stats[k] = {
            'length': len(v),
            'unique_chars': len(set(v)),
            'ratio': len(v) / (len(set(v)) + 1)
        }
    
    # Key computation with distractors
    raw_total = sum(base_map.values())
    bonus = len(outliers) * 1.5
    penalty = dummy_sum // 10 if dummy_sum > 20 else 0
    
    final_score = int(raw_total + bonus - penalty + adjustment)
    return final_score

# Data setup
data = {
    'alpha': 'abc',
    'beta': 'wxyz',
    'gamma': 'pq',
    'delta': 'hello'
}

weights = {
    'alpha': 1.2,
    'beta': 0.8,
    'gamma': 1.5
}

# Execute and print result
result = process_results(data, weights)
print(f"Result: {result}")