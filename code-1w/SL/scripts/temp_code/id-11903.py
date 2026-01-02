def analyze_pattern(sequence):
    count = 0
    trend = []
    for i, val in enumerate(sequence):
        if i > 0 and val > sequence[i-1]:
            count += 1
            trend.append(1)
        elif i > 0 and val < sequence[i-1]:
            trend.append(-1)
        else:
            trend.append(0)
    return count, trend

# Irrelevant helper function (dead weight)
def unused_helper(x):
    return (x ** 2 + 3 * x) % 7

def validate_entry(record):
    if not record.get('active'):
        return False
    score = record.get('score', 0)
    if score < 50:
        return False
    tags = record.get('tags', [])
    if 'deprecated' in tags:
        return False
    return True

def compute_weighted_sum(entries, weights):
    total = 0.0
    debug_logs = []
    for idx, (entry, w) in enumerate(zip(entries, weights)):
        raw_value = entry.get('value', 0)
        adjusted = raw_value * w
        noise_offset = (idx * 0.01)  # negligible but distracting
        total += adjusted + noise_offset
        debug_logs.append(f'Step {idx}: {adjusted}')
    return round(total, 4)

def process_results(data, thresholds):
    valid_items = []
    temp_cache = {}
    for item in data:
        if validate_entry(item):
            key = item['id']
            temp_cache[key] = item['score']
            valid_items.append(item)
    
    # Extract values for processing
    values = [item['value'] for item in valid_items]
    base_sequence = [v % 7 for v in values]
    
    # Real logic starts here
    _, trend_flags = analyze_pattern(base_sequence)
    trend_sum = sum(trend_flags)
    
    weights = [0.1, 0.2, 0.3, 0.4]  # dummy length
    if len(values) >= 4:
        weights = [0.4, 0.3, 0.2, 0.1][:len(values)]
    
    weighted_total = compute_weighted_sum(valid_items, weights)
    
    # Core computation
    threshold_check = sum(1 for v in values if v > thresholds[0])
    penalty = 0
    if len(values) != len(set(values)):
        penalty += 5
    
    # Distracting modular arithmetic
    magic_factor = (len(temp_cache) * 3) % 11
    dummy_calc = (trend_sum * 2 + penalty) % 9
    
    # Actual answer derivation
    base_score = int(weighted_total)
    adjustment = threshold_check * 2
    final_score = base_score + adjustment - penalty
    
    # Red herring: unused intermediate
    diagnostic_key = f"CHK-{magic_factor}-{dummy_calc}"
    
    return final_score

# Setup input
data = [
    {'id': 1, 'score': 65, 'value': 120, 'active': True, 'tags': []},
    {'id': 2, 'score': 70, 'value': 80, 'active': True, 'tags': []},
    {'id': 3, 'score': 45, 'value': 90, 'active': True, 'tags': ['deprecated']},  # filtered out
    {'id': 4, 'score': 80, 'value': 110, 'active': True, 'tags': []},
    {'id': 5, 'score': 90, 'value': 80, 'active': False, 'tags': []},  # filtered out
]
thresholds = [85, 60]

# Execute
count_analysis, _ = analyze_pattern([120, 80, 110, 80])
unused_diagnostic = unused_helper(len(data))
final_score = process_results(data, thresholds)
print(f"Result: {final_score}")