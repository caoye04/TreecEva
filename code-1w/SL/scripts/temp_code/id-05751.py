def analyze_data(records):
    # Irrelevant data transformation (distractor)
    processed = [r['value'] * 2 for r in records if r['active']]
    normalized = [p / sum(processed) for p in processed]
    return normalized

# Simulated sensor metrics with metadata (some fields are red herrings)
metrics = [
    {'name': 'latency', 'value': 85, 'weight': 0.3, 'unit': 'ms', 'critical': True},
    {'name': 'throughput', 'value': 420, 'weight': 0.25, 'unit': 'req/s', 'critical': False},
    {'name': 'error_rate', 'value': 1.2, 'weight': 0.2, 'unit': '%', 'critical': True},
    {'name': 'memory', 'value': 68, 'weight': 0.15, 'unit': 'MB', 'critical': False},
    {'name': 'cpu', 'value': 77, 'weight': 0.1, 'unit': '%', 'critical': True}
]

weights = [m['weight'] for m in metrics]  # Extract weights (relevant)
values = [m['value'] for m in metrics]   # Extract values (relevant)

# Dead code path - never called (distractor)
def legacy_calculate(vectors):
    total = 0
    for v in vectors:
        if v > 50:
            total += v ** 0.5
    return total // 3

# Misleading intermediate calculation (looks important but unused)
avg_metric = sum(values) / len(values)
adjusted_metrics = [v * 1.05 if v < avg_metric else v * 0.95 for v in values]

# Complex normalization function with conditional logic and slicing
def normalize_scores(raw):
    sorted_vals = sorted(raw)
    trimmed = sorted_vals[1:-1]  # Remove outliers (slicing)
    mean_val = sum(trimmed) / len(trimmed)
    return [abs(v - mean_val) for v in raw]

# Weighted scoring with dictionary-based lookup (red herring)
score_map = {i: val//10 for i, val in enumerate(values)}
bonus_lookup = {0: 5, 2: 3, 4: 2}  # Unused bonus table (decoy)

# Core evaluation logic buried among distractions
def evaluate_performance(mets, wts):
    base_scores = []
    for i, m in enumerate(mets):
        val = m['value']
        wt = m['weight']
        # Non-linear penalty for latency and error rate
        if m['name'] == 'latency':
            score = (100 - val) * wt
        elif m['name'] == 'error_rate':
            score = (100 - (val * 10)) * wt
        else:
            score = (val / 10) * wt  # Normalize other metrics
        base_scores.append(score)
    
    # Apply artificial cap and adjustment (key step)
    capped = [min(s, 25) for s in base_scores]
    final_sum = sum(capped)
    
    # Conditional offset based on critical components
    critical_count = len([m for m in mets if m['critical']])
    offset = 5 if critical_count >= 3 else 0
    
    # Final non-linear adjustment
    result = final_sum + offset
    if result > 90:
        result = result * 0.95 + 2
    else:
        result = result * 1.05
    
    return round(result, 4)

# Irrelevant list/dict manipulation (distractor)
temp_data = [{'idx': i, 'chunk': values[i:i+2]} for i in range(0, len(values), 2)]
flat_chunks = [item for chunk in temp_data for item in chunk['chunk']]
duplicate_filter = list(dict.fromkeys(flat_chunks))

# Key execution point
final_score = evaluate_performance(metrics, weights)

# Print required output
print(f"Result: {final_score}")