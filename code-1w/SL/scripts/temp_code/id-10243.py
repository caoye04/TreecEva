import math

# Irrelevant helper function (dead code path)
def unused_helper(x):
    return sum(i ** 2 for i in range(x))

# Misleading metric calculator (used to distract)
def false_metric(values):
    temp = 0
    for v in values:
        if v > 5:
            temp += v * 0.3
    return round(temp, 2)

# Auxiliary transformation (looks important but only partially used)
def transform_sequence(seq):
    transformed = []
    for i, val in enumerate(seq):
        if i % 2 == 0:
            transformed.append(val * 1.5)
        else:
            transformed.append(val - 1)
    return transformed

# Real processing logic buried in distractions
def process_metrics(data, config):
    # Step 1: Extract relevant data
    raw_values = [v['reading'] for v in data if v['active']]
    
    # Step 2: Apply scaling based on config (key step)
    scale_factor = config.get('scale', 1.0)
    scaled = [x * scale_factor for x in raw_values]
    
    # Step 3: Compute moving average over 2 elements (relevant)
    smoothed = []
    for i in range(len(scaled) - 1):
        smoothed.append((scaled[i] + scaled[i+1]) / 2.0)
    
    # Step 4: Filter outliers above threshold (config-based)
    threshold = config.get('threshold', 100)
    filtered = [s for s in smoothed if s <= threshold]
    
    # Step 5: Map categories using dictionary lookup (core concept)
    category_map = {
        'A': 10, 'B': 25, 'C': 18, 'D': 7
    }
    category_scores = []
    for item in data:
        code = item.get('category', 'D')
        multiplier = category_map.get(code, 5)
        # Only contribute if reading was even (hidden condition)
        if item['reading'] % 2 == 0:
            category_scores.append(multiplier)
    
    # Step 6: Accumulate final weighted sum (answer source)
    base_total = sum(filtered)
    bonus = sum(category_scores) * 0.5
    final_score = int(base_total + bonus)  # This is the target variable
    
    # Irrelevant secondary calculations (distractors)
    phantom_sum = sum(math.sin(x) for x in raw_values[:3])
    dummy_dict = {k: v*2 for k, v in enumerate(raw_values) if v < 10}
    _ = [transform_sequence(list(range(n))) for n in [3, 4]]  # Dead computation
    
    return final_score

# Simulated sensor data with mixed attributes
data = [
    {'reading': 8, 'active': True, 'category': 'A'},
    {'reading': 12, 'active': True, 'category': 'B'},
    {'reading': 3, 'active': False, 'category': 'C'},  # inactive
    {'reading': 6, 'active': True, 'category': 'A'},
    {'reading': 15, 'active': True, 'category': 'D'},
    {'reading': 4, 'active': True, 'category': 'B'}
]

# Configuration dict with red herring keys
config = {
    'scale': 1.2,
    'threshold': 14.0,
    'debug': True,
    'max_iters': 100,
    'smoothing_window': 2,
    'use_enhancement': False,
    'legacy_mode': 'off'
}

# Call that produces the result
final_score = process_metrics(data, config)
print(f"Result: {final_score}")