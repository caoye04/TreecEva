def analyze_data(records):
    # Irrelevant data transformation
    temp_stats = {}
    for r in records:
        key = r['type']
        if key not in temp_stats:
            temp_stats[key] = 0
        temp_stats[key] += r['value'] * 0.1

    adjusted_records = []
    for r in records:
        adjusted_records.append({
            'id': r['id'],
            'score': r['value'] + (r['value'] * 0.05)
        })

    return adjusted_records


def filter_outliers(data, threshold=30):
    # Dead code path - never actually used in logic
    clean_data = [x for x in data if x > threshold]
    return clean_data

# Misleading initialization of global-like variables
baseline_offset = 17
reference_points = [1, 2, 3, 4, 5]
useless_counter = 0

# Simulated metrics with red herring computations
raw_metrics = {
    'latency': [120, 135, 105, 150, 98],
    'throughput': [85, 90, 88, 92, 87],
    'errors': [2, 1, 3, 0, 1]
}

# Distractor: complex-looking but unused bit manipulation
bit_flags = 0b1010 ^ 0b1100 & 0b1111
flag_check = (bit_flags << 2) | 0b0011

# Unused recursive function meant to distract
def compute_factorial(n):
    if n <= 1:
        return 1
    return n * compute_factorial(n - 1)

# Actual relevant data structure
metric_set = {
    'accuracy': { 'values': [0.91, 0.89, 0.93, 0.90, 0.92], 'weight': 0.4 },
    'precision': { 'values': [0.87, 0.85, 0.88, 0.90, 0.86], 'weight': 0.3 },
    'recall': { 'values': [0.84, 0.86, 0.83, 0.85, 0.87], 'weight': 0.3 }
}

# Decoy dataset
fake_dataset = set()
for i in range(10):
    fake_dataset.add(i * i % 7)

# Real processing begins here — heavily buried
aggregated = {}
for name, config in metric_set.items():
    values = config['values']
    avg = sum(values) / len(values)
    aggregated[name] = avg

# Compute weighted score — this is the real path
weighted_sum = 0
max_possible = 0
for name, config in metric_set.items():
    weight = config['weight']
    avg_value = aggregated[name]
    weighted_sum += avg_value * weight
    max_possible += 1.0 * weight  # since max metric value is 1.0

normalized_score = weighted_sum / max_possible

# Set operation distraction — looks important but unused
active_components = {'accuracy', 'precision'}
system_modules = {'accuracy', 'precision', 'recall', 'f1'}
redundant_intersection = active_components & system_modules

# Linear search through irrelevant list
search_key = 'timing'
found_index = -1
search_list = ['memory', 'cpu', 'bandwidth', 'timing']
for idx, item in enumerate(search_list):
    if item == search_key:
        found_index = idx
        break  # early break - distractor control flow

# Critical computation buried after distractions
consistency_bonus = 0
for m in metric_set['accuracy']['values']:
    if abs(m - aggregated['accuracy']) < 0.02:
        consistency_bonus += 0.005

# Final performance evaluation — KEY STATEMENT
final_score = evaluate_performance(metric_set)

# Definition placed *after* usage (to confuse execution order)
def evaluate_performance(metrics):
    base_score = 0
    total_weight = 0
    
    for k, v in metrics.items():
        avg_val = sum(v['values']) / len(v['values'])
        base_score += avg_val * v['weight']
        total_weight += v['weight']
    
    result = base_score / total_weight
    
    # Additional adjustment based on precision stability
    precision_vals = metrics['precision']['values']
    precision_set = set(precision_vals)
    if len(precision_set) < len(precision_vals):  # some duplicates -> stable
        result += 0.01
    
    return int(result * 1000) / 1000  # round to 3 decimal places

# Print final answer as required
print(f"Result: {final_score}")